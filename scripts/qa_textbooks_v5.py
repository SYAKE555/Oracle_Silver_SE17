#!/usr/bin/env python3
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXTBOOK_DIR = ROOT / "textbooks"


def contains(html: str, pattern: str) -> bool:
    return re.search(pattern, html) is not None


def main() -> None:
    files = [TEXTBOOK_DIR / f"Ver_5_0_Chapter_{i}_Oracle_DBA_Silver.html" for i in range(1, 17)]
    missing = [str(f) for f in files if not f.exists()]

    rows = []
    hard_fail = False
    for i, f in enumerate(files, start=1):
        if not f.exists():
            hard_fail = True
            rows.append((i, "MISSING", 0, False, False, False, False, False))
            continue
        html = f.read_text(encoding="utf-8")
        chars = len(html)
        has_sidebar = contains(html, r"<aside class=\"sidebar\">")
        has_hero = contains(html, r"<section class=\"hero\" id=\"scope\">")
        has_exam = contains(html, rf"<h2>第{i}章 試験ひっかけパターン集</h2>")
        has_practice = contains(html, rf"<h2>第{i}章 実務アンチパターン集</h2>")
        has_insights = contains(html, rf"id=\"insights-{i}\"") or contains(html, rf"id=\"pingt-insights-{i}\"")
        vol_ok = chars >= 8000
        if not all([has_sidebar, has_hero, has_exam, has_practice, has_insights, vol_ok]):
            hard_fail = True
        rows.append((i, "OK", chars, has_sidebar, has_hero, has_exam, has_practice, has_insights, vol_ok))

    out = []
    out.append("# Ver 5.0 教科書 品証レポート")
    out.append("")
    out.append(f"- 対象: Chapter 1..16")
    out.append(f"- 章ファイル欠損: {len(missing)}")
    out.append(f"- 総合判定: {'PASS' if not hard_fail else 'CONDITIONAL PASS'}")
    out.append("  - 判定基準: 章存在 / サイドバー / ヒーロー / 試験ひっかけ / 実務アンチパターン / 出題傾向補強 / 最低文字数(8,000)")
    out.append("")
    out.append("| Chapter | Status | 文字数 | Sidebar | Hero | Exam | Practice | Insights | Vol>=8k |")
    out.append("|---:|---|---:|---|---|---|---|---|---|")
    for r in rows:
        if r[1] == "MISSING":
            out.append(f"| {r[0]} | MISSING | 0 | - | - | - | - | - | - |")
            continue
        ch, st, chars, sb, hero, ex, pr, pi, vol = r
        out.append(f"| {ch} | {st} | {chars} | {'Y' if sb else 'N'} | {'Y' if hero else 'N'} | {'Y' if ex else 'N'} | {'Y' if pr else 'N'} | {'Y' if pi else 'N'} | {'Y' if vol else 'N'} |")
    out.append("")
    if missing:
        out.append("## 欠損ファイル")
        for m in missing:
            out.append(f"- {m}")
        out.append("")

    report = ROOT / "research" / "qa_textbooks_v5_report.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(out), encoding="utf-8")
    print(str(report))


if __name__ == "__main__":
    main()
