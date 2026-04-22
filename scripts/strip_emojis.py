#!/usr/bin/env python3
"""Remove emojis from mock-exam / EX pages and builder scripts I authored."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TARGETS = [
    "dist/mock_exam_report.html",
    "dist/mock_exam_reinforce.html",
    "textbooks/mock_exam_report.html",
    "textbooks/mock_exam_reinforce.html",
] + [f"dist/EX{i}_reinforce.html" for i in range(1, 9)] \
  + [f"textbooks/EX{i}_reinforce.html" for i in range(1, 9)] \
  + ["scripts/build_mock_report.py", "scripts/split_ex_pages.py"]

# Only the section of index.html containing mock-exam/EX cards
INDEX_TARGETS = ["dist/index.html", "textbooks/index.html"]

# Characters to strip (emojis used in my pages)
EMOJIS = ["📊", "📈", "📝", "🎯", "📚", "🔥", "📌", "✅", "⚠", "🗂", "→"]
# Keep ← for back-nav visual, but remove its emoji-arrow counterpart → from cards

# Use regex to strip all non-ASCII pictographs we introduced
PATTERN = re.compile("|".join(re.escape(c) for c in EMOJIS))


def clean(text: str) -> str:
    # Remove emoji characters
    cleaned = PATTERN.sub("", text)
    # Tidy up double spaces created by removal inside tags/labels
    cleaned = re.sub(r"  +", " ", cleaned)
    # Clean ">  <" patterns and leading spaces right after > (where emoji was)
    cleaned = re.sub(r">\s+([^<])", r">\1", cleaned)
    # Clean "content: \"\"" that CSS had (was content: "⚠")
    cleaned = cleaned.replace('content: "";', 'content: "";')
    return cleaned


# Restore specific CSS / replace stripped arrow nav with plain text
def post_fix(text: str, path: str) -> str:
    # .mistake-list li::before used content: "⚠"; now becomes content: "";
    # Replace with a dash prefix instead
    text = text.replace('content: "";', 'content: "!";')
    # nav-back has "← 結果レポート" — ← is kept. Just collapse spacing.
    return text


for rel in TARGETS:
    p = ROOT / rel
    if not p.exists():
        print(f"skip (missing): {rel}")
        continue
    t = p.read_text(encoding="utf-8")
    n = post_fix(clean(t), rel)
    if n != t:
        p.write_text(n, encoding="utf-8")
        print(f"cleaned: {rel}")
    else:
        print(f"no-op: {rel}")


# For index.html, only clean section between our markers
for rel in INDEX_TARGETS:
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    start_marker = '<div class="section-heading" style="border-left-color:#2c3e50">'
    end_marker = '<div class="section-heading">SQL Silver'
    s = t.find(start_marker)
    e = t.find(end_marker)
    if s < 0 or e < 0:
        print(f"skip markers not found: {rel}")
        continue
    section_before = t[:s]
    section = t[s:e]
    section_after = t[e:]
    section_clean = clean(section)

    # Also clean the EX section that comes later
    ex_start = '<div class="section-heading" style="border-left-color:#4a00e0">'
    ex_end_marker = '<div class="section-heading">DBA 参考資料</div>'
    # Handle both in section_after
    es = section_after.find(ex_start)
    ee = section_after.find(ex_end_marker)
    if es >= 0 and ee >= 0:
        ex_section = section_after[es:ee]
        ex_clean = clean(ex_section)
        section_after = section_after[:es] + ex_clean + section_after[ee:]

    new = section_before + section_clean + section_after
    if new != t:
        p.write_text(new, encoding="utf-8")
        print(f"cleaned index: {rel}")
