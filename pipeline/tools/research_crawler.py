#!/usr/bin/env python3
"""
Basetract Research Crawler — Fixed Version
修正点:
  - soup.find_all(['dl', 'div[class*="list"]', ...]) が誤り（BeautifulSoupのfind_allは
    CSSセレクタ文字列を受け付けない）→ soup.find_all() + soup.select() に分離して修正
  - ul/ol からナビゲーション要素を除外するヒューリスティックを追加
  - div グリッドの cell 抽出でリスト内包テキストが入っていなかったバグを修正
  - _persist_data の重複ファイル名リスクを uuid に変更
"""
import requests
from bs4 import BeautifulSoup
import json
import os
import uuid
import logging
import re
import time
import random
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# ナビゲーション用ul/olを除外するための親要素セレクタ
NAV_PARENT_TAGS = {'nav', 'header', 'footer'}
# ナビゲーション用クラス名パターン
NAV_CLASS_PATTERN = re.compile(r'nav|menu|breadcrumb|footer|header|sidebar', re.IGNORECASE)

# 中央化ネットワーク設定からUser-Agentプールを取得
from network_config import NetworkConfig, get_timeout
USER_AGENTS = NetworkConfig.get_crawler_config()["user_agents"]
BLOCKED_PATTERNS = NetworkConfig.get_crawler_config()["blocked_patterns"]


class ResearchPipeline:
    """公式ドキュメントURLから技術データを収集するパイプライン。"""

    def __init__(self, output_dir: str = None):
        # 設定または引数から出力先を決定
        self.output_dir = output_dir or os.getenv("BASETRACT_DATA_STAGE", "pipeline/data_stage")
        
        # 中央化クローラー設定を取得
        crawler_config = NetworkConfig.get_crawler_config()
        self.min_delay = crawler_config["min_delay"]
        self.max_delay = crawler_config["max_delay"]
        self.last_request_time = 0.0
        
        # Session configuration
        self.session = requests.Session()
        self._rotate_user_agent()
        
        # セッション設定の改善
        self.session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',  # Do Not Track
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        os.makedirs(self.output_dir, exist_ok=True)

    def _rotate_user_agent(self) -> None:
        """User-Agentをランダムにローテーションする。"""
        user_agent = random.choice(USER_AGENTS)
        self.session.headers.update({'User-Agent': user_agent})

    def _rate_limit(self) -> None:
        """レート制限: 前回リクエストからの待機時間を確保する。"""
        current_time = time.time()
        elapsed = current_time - self.last_request_time
        
        if elapsed < self.min_delay:
            wait_time = self.min_delay - elapsed
            logger.info(f"Rate limiting: waiting {wait_time:.1f}s")
            time.sleep(wait_time)
        
        # 次回リクエストのためのランダム遅延
        additional_delay = random.uniform(0, self.max_delay - self.min_delay)
        if additional_delay > 0:
            time.sleep(additional_delay)
        
        self.last_request_time = time.time()

    def ingest_url(self, url: str) -> None:
        # SSRF保護: プロトコル検証
        if not url.startswith(('http://', 'https://')):
            logger.error(f"Insecure protocol rejected: {url}")
            return

        # SSRF保護: ホスト名を抽出してから内部IPパターンをチェック
        # ← バグ修正: URLをそのまま検索すると r'^10\.' が http://10.x.x.x を
        #   ブロックできない（URLは 'http://' で始まるため ^ が機能しない）
        try:
            hostname = urlparse(url).hostname or ''
        except Exception:
            logger.error(f"Failed to parse URL: {url}")
            return

        local_patterns = BLOCKED_PATTERNS
        if any(re.search(p, hostname, re.IGNORECASE) for p in local_patterns):
            logger.error(f"Internal network target rejected (hostname={hostname!r}): {url}")
            return

        logger.info(f"Ingesting resource: {url}")
        
        # レート制限、User-Agentローテーション、および robots.txt 整合性確認
        self._rate_limit()
        self._rotate_user_agent()
        self._check_robots_txt(url)
        
        try:
            request_timeout = get_timeout("crawler_request")
            response = self.session.get(url, timeout=request_timeout)
            response.raise_for_status()

            # SPA検出（静的取得の限界を警告）
            spa_markers = ['app-root', 'ng-app', 'react-data', 'vue-root', '__next']
            if any(m in response.text.lower() for m in spa_markers):
                logger.warning("SPA/JS-Rendering detected. Content may be incomplete.")
                logger.warning("Resolution: Use Playwright/Selenium for full rendering.")

            soup = BeautifulSoup(response.text, 'html.parser')
            segment_count = 0

            # ── 1. テーブルデータ ──────────────────────────────
            for i, table in enumerate(soup.find_all('table')):
                rows = [
                    [c.get_text(separator=' ', strip=True) for c in tr.find_all(['td', 'th'])]
                    for tr in table.find_all('tr')
                    if tr.find_all(['td', 'th'])
                ]
                if rows:
                    self._persist_data(rows, f"table_segment_{i}")
                    segment_count += 1

            # div ベースのグリッド（CSSセレクタは soup.select() を使う）
            for i, grid in enumerate(soup.select('div[class*="grid"], div[class*="table-row"]')):
                cells = grid.find_all('div', class_=re.compile(r'cell|col|item', re.IGNORECASE))
                if len(cells) >= 2:
                    rows = [[c.get_text(strip=True) for c in cells]]
                    self._persist_data(rows, f"grid_segment_{i}")
                    segment_count += 1

            # ── 2. 定義リスト（dl/dt/dd） ───────────────────────
            for i, dl in enumerate(soup.find_all('dl')):
                items = [
                    [dt.get_text(strip=True), dd.get_text(strip=True)]
                    for dt, dd in zip(dl.find_all('dt'), dl.find_all('dd'))
                    if dt.get_text(strip=True) and dd.get_text(strip=True)
                ]
                if items:
                    self._persist_data(items, f"definition_segment_{i}")
                    segment_count += 1

            # ── 3. 技術用リスト（ul/ol）── ナビゲーション要素を除外 ──
            for i, lst in enumerate(soup.find_all(['ul', 'ol'])):
                if self._is_navigation_list(lst):
                    continue
                items = [
                    li.get_text(separator=' ', strip=True)
                    for li in lst.find_all('li', recursive=False)
                    if li.get_text(strip=True)
                ]
                # 最低2件 + 平均20文字以上の項目のみ技術コンテンツとして採用
                if len(items) >= 2 and (sum(len(t) for t in items) / len(items)) >= 20:
                    self._persist_data(items, f"list_segment_{i}")
                    segment_count += 1

            logger.info(f"Ingestion complete. {segment_count} segments persisted.")

        except requests.RequestException as e:
            logger.error(f"HTTP request failed: {e}")
        except Exception as e:
            logger.error(f"Ingestion failure: {e}")

    def _check_robots_txt(self, url: str) -> None:
        """robots.txt を確認し、クロール禁止設定を警告する。"""
        from urllib.robotparser import RobotFileParser
        try:
            parsed_url = urlparse(url)
            robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
            rp = RobotFileParser()
            rp.set_url(robots_url)
            rp.read()
            if not rp.can_fetch(self.session.headers.get('User-Agent', '*'), url):
                logger.warning(f"Robots.txt restricted: {url}. Proceeding with caution.")
        except Exception as e:
            logger.debug(f"Could not parse robots.txt: {e}")

    def _is_navigation_list(self, tag) -> bool:
        """ナビゲーション/メニュー用のリストかどうかをヒューリスティックで判定する。"""
        # 親要素のタグ名チェック
        for parent in tag.parents:
            if parent.name in NAV_PARENT_TAGS:
                return True
            if parent.name and parent.get('class'):
                classes = ' '.join(parent.get('class', []))
                if NAV_CLASS_PATTERN.search(classes):
                    return True
            if parent.name == 'body':
                break
        # 要素自身のclass/idチェック
        own_classes = ' '.join(tag.get('class', [])) + ' ' + (tag.get('id') or '')
        return bool(NAV_CLASS_PATTERN.search(own_classes))

    def _persist_data(self, data: list, label: str) -> None:
        """データをJSONファイルに保存する。ファイル名はuuidで衝突回避。"""
        filename = f"{label}_{uuid.uuid4().hex[:6]}.json"
        path = os.path.join(self.output_dir, filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"Persisted: {path} ({len(data)} rows)")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        logger.error("Usage: python3 research_crawler.py <url>")
        sys.exit(1)
    pipeline = ResearchPipeline()
    pipeline.ingest_url(sys.argv[1])
