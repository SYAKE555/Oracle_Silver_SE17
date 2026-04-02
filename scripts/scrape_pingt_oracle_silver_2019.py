#!/usr/bin/env python3
import argparse
import json
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Tuple

import requests
from bs4 import BeautifulSoup


BASE = "https://mondai.ping-t.com"
SUBJECT_ID = 61  # Oracle Master Silver SQL 2019(1Z0-071)


def clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def login(session: requests.Session, username: str, password: str) -> None:
    signin_url = f"{BASE}/users/sign_in"
    r = session.get(signin_url, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    token_el = soup.select_one("form#new_user input[name='authenticity_token']")
    if not token_el or not token_el.get("value"):
        raise RuntimeError("ログインフォームのauthenticity_tokenが見つかりません。")

    payload = {
        "authenticity_token": token_el["value"],
        "user[login_key]": username,
        "user[password]": password,
        "user[remember_me]": "1",
        "commit": "ログイン",
    }
    r2 = session.post(signin_url, data=payload, allow_redirects=True, timeout=30)
    r2.raise_for_status()

    # session_gateが出る場合
    if "/session_gate" in r2.url:
        soup2 = BeautifulSoup(r2.text, "html.parser")
        form = soup2.select_one("form.button_to[action='/session_gate/continue']")
        if form:
            gate_token_el = form.select_one("input[name='authenticity_token']")
            if gate_token_el and gate_token_el.get("value"):
                session.post(
                    f"{BASE}/session_gate/continue",
                    data={"authenticity_token": gate_token_el["value"]},
                    allow_redirects=True,
                    timeout=30,
                ).raise_for_status()

    # ログイン確認
    r3 = session.get(f"{BASE}/g/question_subjects", timeout=30)
    r3.raise_for_status()
    if "ログイン" in r3.text and "ログアウト" not in r3.text and "でログイン中" not in r3.text:
        raise RuntimeError("ログイン判定に失敗しました。資格情報または追加認証条件を確認してください。")


def get_total_pages(session: requests.Session) -> int:
    url = f"{BASE}/question_subjects/{SUBJECT_ID}/questions"
    r = session.get(url, params={"q[include_reference]": "1"}, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    page_nums = []
    for a in soup.select("ul.pagination a.page-link"):
        txt = clean_text(a.get_text())
        if txt.isdigit():
            page_nums.append(int(txt))
        href = a.get("href") or ""
        m = re.search(r"[?&]page=(\d+)", href)
        if m:
            page_nums.append(int(m.group(1)))
    return max(page_nums) if page_nums else 1


def collect_question_links(session: requests.Session, total_pages: int) -> List[str]:
    links: List[str] = []
    seen = set()
    for page in range(1, total_pages + 1):
        params = {"q[include_reference]": "1", "page": str(page)}
        r = session.get(f"{BASE}/question_subjects/{SUBJECT_ID}/questions", params=params, timeout=30)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        for a in soup.select(f"a[href^='/question_subjects/{SUBJECT_ID}/questions/']"):
            href = a.get("href") or ""
            m = re.search(rf"/question_subjects/{SUBJECT_ID}/questions/(\d+)", href)
            if not m:
                continue
            qid = m.group(1)
            full = f"{BASE}/question_subjects/{SUBJECT_ID}/questions/{qid}?q%5Binclude_reference%5D=1"
            if full not in seen:
                seen.add(full)
                links.append(full)
    return links


def parse_question_page(html: str, source_url: str) -> Dict:
    soup = BeautifulSoup(html, "html.parser")

    qid = None
    branch = None
    q_meta = soup.select_one("ul.list-inline li.list-inline-item")
    if q_meta:
        num = q_meta.select_one("span.text-roman-number")
        if num:
            qid = clean_text(num.get_text())
        spans = q_meta.find_all("span")
        if len(spans) >= 2:
            branch = clean_text(spans[-1].get_text())

    # 問題文: 履歴ブロック/選択肢/正解・解説・参考を除いた最初の本文候補
    question_text = ""
    qroot = soup.select_one("div.question div.container")
    if qroot:
        for block in qroot.select("div.mb-6"):
            txt = clean_text(block.get_text(" ", strip=True))
            if not txt:
                continue
            if len(txt) < 15:
                continue
            if any(ng in txt for ng in ["履歴", "正解", "解説", "参考URL", "参考"]):
                continue
            # 選択肢のみの塊を除外（先頭がSELECTで始まりやすい）
            if txt.startswith("SELECT ") and "どれ" not in txt and "何" not in txt:
                continue
            question_text = txt
            break

    explanation = ""
    correct = soup.select_one("#correct .card-body")
    if correct:
        # 「解説」strongの次のdivを優先
        for p in correct.find_all("p"):
            if "解説" in p.get_text():
                nxt = p.find_next_sibling()
                if nxt:
                    explanation = clean_text(nxt.get_text(" ", strip=True))
                    break
        if not explanation:
            explanation = clean_text(correct.get_text(" ", strip=True))

    ref_urls: List[str] = []
    ref_titles: List[str] = []
    ref_sec = soup.select_one("#reference-url .card-body")
    if ref_sec:
        for a in ref_sec.select("a[href]"):
            href = clean_text(a.get("href", ""))
            if href:
                ref_urls.append(href)
                ref_titles.append(clean_text(a.get_text(" ", strip=True)))

    if not qid:
        m = re.search(rf"/question_subjects/{SUBJECT_ID}/questions/(\d+)", source_url)
        qid = m.group(1) if m else ""

    return {
        "question_id": int(qid) if str(qid).isdigit() else None,
        "branch": branch or "",
        "question_text": question_text,
        "explanation": explanation,
        "reference_urls": ref_urls,
        "reference_titles": ref_titles,
        "source_url": source_url,
    }


def build_trend_summary(rows: List[Dict]) -> Dict[str, Dict]:
    per_branch = defaultdict(list)
    for r in rows:
        per_branch[r["branch"] or "不明"].append(r)

    out: Dict[str, Dict] = {}
    keyword_patterns = [
        "SELECT", "WHERE", "GROUP BY", "HAVING", "ORDER BY", "JOIN", "副問合せ",
        "UNION", "INSERT", "UPDATE", "DELETE", "MERGE", "CREATE", "ALTER", "DROP",
        "TRUNCATE", "VIEW", "INDEX", "SEQUENCE", "GRANT", "REVOKE", "TIMESTAMP", "INTERVAL",
    ]
    for branch, items in per_branch.items():
        text = " ".join((i.get("question_text", "") + " " + i.get("explanation", "")) for i in items)
        hit = [k for k in keyword_patterns if k in text]
        out[branch] = {
            "question_count": len(items),
            "keyword_hits": hit,
            "reference_url_count": sum(len(i.get("reference_urls", [])) for i in items),
        }
    return out


def save_sqlite(db_path: Path, rows: List[Dict], trend: Dict[str, Dict]) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS pingt_questions (
          question_id INTEGER PRIMARY KEY,
          branch TEXT,
          question_text TEXT,
          explanation TEXT,
          reference_urls_json TEXT,
          reference_titles_json TEXT,
          source_url TEXT
        )
        """
    )
    cur.execute("DELETE FROM pingt_questions")
    for r in rows:
        cur.execute(
            """
            INSERT OR REPLACE INTO pingt_questions
            (question_id, branch, question_text, explanation, reference_urls_json, reference_titles_json, source_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                r["question_id"],
                r["branch"],
                r["question_text"],
                r["explanation"],
                json.dumps(r["reference_urls"], ensure_ascii=False),
                json.dumps(r["reference_titles"], ensure_ascii=False),
                r["source_url"],
            ),
        )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS pingt_branch_trends (
          branch TEXT PRIMARY KEY,
          question_count INTEGER,
          keyword_hits_json TEXT,
          reference_url_count INTEGER
        )
        """
    )
    cur.execute("DELETE FROM pingt_branch_trends")
    for branch, t in trend.items():
        cur.execute(
            """
            INSERT OR REPLACE INTO pingt_branch_trends
            (branch, question_count, keyword_hits_json, reference_url_count)
            VALUES (?, ?, ?, ?)
            """,
            (branch, t["question_count"], json.dumps(t["keyword_hits"], ensure_ascii=False), t["reference_url_count"]),
        )
    con.commit()
    con.close()


def save_binder_md(md_path: Path, rows: List[Dict], trend: Dict[str, Dict]) -> None:
    now = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    total_refs = sum(len(r["reference_urls"]) for r in rows)
    lines = [
        "# Ping-t Oracle Master Silver SQL 2019 参考資料バインダー",
        "",
        f"- 作成日時: {now}",
        f"- 取得対象: `https://mondai.ping-t.com/question_subjects/{SUBJECT_ID}`",
        f"- 取得問題数: **{len(rows)}**",
        f"- 取得参考URL数: **{total_refs}**",
        "",
        "## 分野別傾向サマリ",
        "",
        "| 分野 | 問題数 | 参考URL数 | 傾向キーワード |",
        "|---|---:|---:|---|",
    ]
    for branch, t in sorted(trend.items(), key=lambda x: x[1]["question_count"], reverse=True):
        kws = ", ".join(t["keyword_hits"][:10])
        lines.append(f"| {branch} | {t['question_count']} | {t['reference_url_count']} | {kws} |")

    lines += ["", "## 問題別データ", ""]
    for r in sorted(rows, key=lambda x: x["question_id"] or 0):
        lines.append(f"### 問題ID {r['question_id']} ({r['branch']})")
        lines.append(f"- 問題URL: {r['source_url']}")
        lines.append(f"- 問題傾向: {r['branch']}")
        qtxt = r["question_text"][:300].replace("\n", " ")
        ext = "..." if len(r["question_text"]) > 300 else ""
        lines.append(f"- 問題文要約: {qtxt}{ext}")
        ex = r["explanation"][:500].replace("\n", " ")
        exext = "..." if len(r["explanation"]) > 500 else ""
        lines.append(f"- 解説要約: {ex}{exext}")
        if r["reference_urls"]:
            lines.append("- 参考URL:")
            for u in r["reference_urls"]:
                lines.append(f"  - {u}")
        else:
            lines.append("- 参考URL: なし")
        lines.append("")

    md_path.write_text("\n".join(lines), encoding="utf-8")


def save_chapter_enrichment(md_path: Path, trend: Dict[str, Dict]) -> None:
    # Ping-t分野 -> 教科書章 の対応
    mapping = [
        ("リレーショナル・データベース", 1),
        ("Select文", 2),
        ("データの制限およびソート", 3),
        ("単一行関数", 4),
        ("変換関数および条件式", 5),
        ("グループ関数", 6),
        ("複数の表のデータ", 7),
        ("副問合せ", 8),
        ("集合演算子", 9),
        ("DML文", 10),
        ("DDL文", 11),
        ("ビュー", 12),
        ("索引、シノニムおよびシーケンス", 13),
        ("ユーザ・アクセスの制御", 14),
        ("データ・ディクショナリ・ビュー", 15),
        ("異なるタイム・ゾーンでのデータ管理", 16),
    ]
    lines = [
        "# Ver 5.0 教科書 章別補強データ (Ping-t抽出ベース)",
        "",
        "以下はPing-t問題傾向を章へ反映するための補強ポイントです。",
        "",
    ]
    for branch, chap in mapping:
        t = trend.get(branch, {"question_count": 0, "keyword_hits": [], "reference_url_count": 0})
        lines.append(f"## 第{chap}章向け補強 ({branch})")
        lines.append(f"- 収集問題数: {t['question_count']}")
        lines.append(f"- 参考URL数: {t['reference_url_count']}")
        lines.append(f"- 重点キーワード: {', '.join(t['keyword_hits'][:12]) if t['keyword_hits'] else '（抽出なし）'}")
        lines.append("- 追記推奨:")
        lines.append("  - 試験ひっかけで出題頻度の高い条件差分を追加")
        lines.append("  - 典型誤答パターンと誤答理由を追加")
        lines.append("  - 実務での再現シナリオと検証SQLを追加")
        lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--password", required=True)
    parser.add_argument("--out-dir", default="research/pingt_oracle_silver_2019")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; CodexAgent/1.0)"})

    login(session, args.username, args.password)
    total_pages = get_total_pages(session)
    links = collect_question_links(session, total_pages)

    rows: List[Dict] = []
    for i, url in enumerate(links, start=1):
        r = session.get(url, timeout=30)
        r.raise_for_status()
        row = parse_question_page(r.text, url)
        rows.append(row)
        if i % 50 == 0:
            print(f"[progress] fetched {i}/{len(links)} questions")

    rows = [r for r in rows if r.get("question_id") is not None]
    rows.sort(key=lambda x: x["question_id"])
    trend = build_trend_summary(rows)

    json_path = out_dir / "questions.json"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    save_sqlite(out_dir / "learning_explanations.db", rows, trend)
    save_binder_md(out_dir / "reference_binder.md", rows, trend)
    save_chapter_enrichment(out_dir / "chapter_enrichment_plan.md", trend)

    summary = {
        "subject_id": SUBJECT_ID,
        "question_count": len(rows),
        "total_pages": total_pages,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "branch_counts": dict(sorted(((k, v["question_count"]) for k, v in trend.items()), key=lambda x: x[0])),
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
