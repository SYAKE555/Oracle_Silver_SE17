#!/usr/bin/env python3
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "research" / "pingt_oracle_silver_2019" / "questions.json"
TEXTBOOK_DIR = ROOT / "textbooks"


def load_rows():
    return json.loads(DATA.read_text(encoding="utf-8"))


def main():
    rows = load_rows()
    by_branch = defaultdict(list)
    for r in rows:
        by_branch[r.get("branch", "")].append(r)

    chapter_map = {
        1: "リレーショナル・データベース",
        2: "Select文",
        3: "データの制限およびソート",
        4: "単一行関数",
        5: "変換関数および条件式",
        6: "グループ関数",
        7: "複数の表のデータ",
        8: "副問合せ",
        9: "集合演算子",
        10: "DML文",
        11: "DDL文",
        12: "ビュー",
        13: "索引、シノニムおよびシーケンス",
        14: "ユーザ・アクセスの制御",
        15: "データ・ディクショナリ・ビュー",
        16: "異なるタイム・ゾーンでのデータ管理",
    }

    keyword_candidates = [
        "SELECT", "WHERE", "GROUP BY", "HAVING", "ORDER BY", "JOIN", "副問合せ",
        "UNION", "INSERT", "UPDATE", "DELETE", "MERGE", "CREATE", "ALTER", "DROP",
        "TRUNCATE", "VIEW", "INDEX", "SEQUENCE", "GRANT", "REVOKE", "TIMESTAMP", "INTERVAL",
    ]

    for chap, branch in chapter_map.items():
        path = TEXTBOOK_DIR / f"Ver_5_0_Chapter_{chap}_Oracle_DBA_Silver.html"
        if not path.exists():
            continue
        html = path.read_text(encoding="utf-8")
        marker = f'id="pingt-insights-{chap}"'
        if marker in html:
            continue

        items = by_branch.get(branch, [])
        qcount = len(items)
        ref_urls = []
        for it in items:
            ref_urls.extend(it.get("reference_urls", []))
        # 重複排除
        seen = set()
        uniq_refs = []
        for u in ref_urls:
            if u and u not in seen:
                seen.add(u)
                uniq_refs.append(u)
        sample_refs = uniq_refs[:3]

        text_blob = " ".join((it.get("question_text", "") + " " + it.get("explanation", "")) for it in items)
        hit_keywords = [k for k in keyword_candidates if k in text_blob][:10]
        hit_kw_text = " / ".join(hit_keywords) if hit_keywords else "抽出なし"

        refs_html = "".join(f"<li><a href=\"{u}\" target=\"_blank\" rel=\"noopener noreferrer\">{u}</a></li>" for u in sample_refs)
        if not refs_html:
            refs_html = "<li>参照URLなし</li>"

        snippet = f"""
    <section class="card" id="pingt-insights-{chap}">
      <h2>Ping-t傾向補強（第{chap}章）</h2>
      <p>Ping-t「Oracle Master Silver SQL 2019」収集データに基づく第{chap}章対応分野「{branch}」の傾向補強である。収集問題数は{qcount}問で、出題傾向の核は「{hit_kw_text}」に集中する。試験対策では、構文暗記よりも条件差分と失敗時挙動の判定を優先することで正答率が上がる。実務では、同テーマに対して確認SQLと本実行SQLを対にして扱うと事故率を下げられる。</p>
      <div class="note"><strong>補強方針:</strong> 本章の例題を解く際は、同じ概念を「成功例」「失敗例」「修正例」の3パターンで比較し、判定根拠を言語化すること。</div>
      <p><strong>参照URL例（Ping-t解説由来）:</strong></p>
      <ul>
        {refs_html}
      </ul>
      <div class="top"><a href="#scope">▲ トップへ戻る</a></div>
    </section>
"""

        html = html.replace('<section class="card" id="exam">', snippet + '\n    <section class="card" id="exam">', 1)
        path.write_text(html, encoding="utf-8")
        print(f"updated: {path}")


if __name__ == "__main__":
    main()
