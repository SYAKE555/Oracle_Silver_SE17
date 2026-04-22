#!/usr/bin/env python3
"""Split mock_exam_reinforce.html into independent EX1..EX8 pages.

Priority order (weakest domain first) maps to EX number:
  EX1=D5, EX2=D6, EX3=D3, EX4=D7, EX5=D8, EX6=D4, EX7=D1, EX8=D2
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = (ROOT / "dist" / "mock_exam_reinforce.html").read_text(encoding="utf-8")

# Extract <style>...</style>
style_match = re.search(r"<style>.*?</style>", SRC, re.DOTALL)
STYLE = style_match.group(0)

# Extract each domain-block by id
BLOCK_RE = re.compile(
    r'<!-- (D\d) -->\s*<div class="domain-block" id="(d\d)"[^>]*>(.*?)</div>\s*(?=<!-- D\d -->|<div style="text-align:center)',
    re.DOTALL,
)

blocks = {}
for m in BLOCK_RE.finditer(SRC):
    dom = m.group(1)  # D5
    inner = m.group(3)  # inside the domain-block div
    # Reconstruct the outer <div> wrapper but preserve style attribute
    full_match = re.search(
        rf'<div class="domain-block" id="{m.group(2)}"[^>]*>.*?</div>\s*(?=<!-- D\d -->|<div style="text-align:center)',
        SRC, re.DOTALL,
    )
    blocks[dom] = full_match.group(0) if full_match else None

# Priority order EX N -> (domain, label, priority class)
EX_ORDER = [
    ("EX1", "D5", "複数表の結合", "high"),
    ("EX2", "D6", "サブクエリ・集合演算", "high"),
    ("EX3", "D3", "単一行関数", "mid"),
    ("EX4", "D7", "DML・トランザクション", "mid"),
    ("EX5", "D8", "DDL・オブジェクト管理", "mid"),
    ("EX6", "D4", "グループ関数・集計", "low"),
    ("EX7", "D1", "SQLとRDBの基礎", "low"),
    ("EX8", "D2", "データの絞り込みとソート", "ok"),
]

PRIORITY_COLOR = {"high": "#c0392b", "mid": "#e67e22", "low": "#f1c40f", "ok": "#2ecc71"}
PRIORITY_LABEL = {"high": "最優先", "mid": "優先", "low": "要復習", "ok": "維持"}


def make_page(ex_id: str, dom: str, label: str, prio: str, block_html: str) -> str:
    color = PRIORITY_COLOR[prio]
    nav = (
        '<a class="nav-back" href="mock_exam_report.html">← 結果レポート</a>'
        '<a class="nav-back" href="index.html" style="margin-left:8px">📚 教科書トップ</a>'
        '<a class="nav-back" href="mock_exam_reinforce.html" style="margin-left:8px">🗂 EX 一覧</a>'
    )
    # Replace the EX tag at the top of the block
    header_banner = f"""
    <div style="background:linear-gradient(135deg,{color}15,{color}08);border-radius:12px;padding:18px 22px;margin-bottom:20px;border-left:6px solid {color}">
      <div style="font-size:.85rem;color:{color};font-weight:700;letter-spacing:.1em">{ex_id} / 弱点強化ユニット（独立）</div>
      <div style="font-size:1.4rem;font-weight:800;margin-top:4px">{label}</div>
      <div style="font-size:.85rem;color:#718096;margin-top:4px">元ドメイン: {dom} ／ 優先度: <b style="color:{color}">{PRIORITY_LABEL[prio]}</b></div>
    </div>
    """
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{ex_id} {label} - 弱点強化ユニット</title>
{STYLE}
</head>
<body>
<div class="page-header" style="background:linear-gradient(135deg,#2c3e50 0%,{color} 100%)">
  <h1>{ex_id} 弱点強化ユニット</h1>
  <div class="subtitle">{label}（独立EXユニット）</div>
</div>
<div class="container">
  {nav}
  {header_banner}
  {block_html}
  <div style="margin-top:20px;padding:14px 18px;background:white;border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,.06);font-size:.88rem;color:#4a5568">
    <b>次のユニット：</b> <a href="mock_exam_reinforce.html">🗂 EX 一覧へ戻る</a>
  </div>
  <div style="text-align:center;color:#a0aec0;font-size:.78rem;margin-top:30px;padding-top:16px;border-top:1px solid #e2e8f0">
    {ex_id} / 弱点強化ユニット — 模擬試験 Phase 2
  </div>
</div>
</body>
</html>
"""


# Also rebuild mock_exam_reinforce.html as an EX index page
def make_ex_index() -> str:
    cards = ""
    for ex_id, dom, label, prio in EX_ORDER:
        color = PRIORITY_COLOR[prio]
        cards += f"""
    <a class="ex-card" href="{ex_id}_reinforce.html" style="border-left:6px solid {color}">
      <div class="ex-tag" style="background:{color}">{ex_id}</div>
      <div class="ex-body">
        <div class="ex-title">{label}</div>
        <div class="ex-meta">優先度 <b style="color:{color}">{PRIORITY_LABEL[prio]}</b> ／ 元ドメイン {dom}</div>
      </div>
      <div class="ex-arrow">→</div>
    </a>"""
    extra_style = """
    .ex-grid { display: grid; gap: 12px; }
    .ex-card { display: grid; grid-template-columns: 70px 1fr 30px; gap: 14px; align-items: center; padding: 14px 18px; background: white; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,.06); text-decoration: none; color: #2d3748; transition: transform .15s, box-shadow .15s; }
    .ex-card:hover { transform: translateY(-2px); box-shadow: 0 4px 14px rgba(0,0,0,.1); }
    .ex-tag { color: white; font-weight: 900; text-align: center; padding: 8px 0; border-radius: 8px; font-size: 1rem; letter-spacing: .05em; }
    .ex-title { font-weight: 700; font-size: 1rem; }
    .ex-meta { font-size: .82rem; color: #718096; margin-top: 3px; }
    .ex-arrow { font-size: 1.4rem; color: #a0aec0; text-align: center; }
    """
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EX 弱点強化ユニット一覧 - Oracle Silver SQL</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', 'Hiragino Sans', Arial, sans-serif; background: #f5f7fa; color: #2d3748; line-height: 1.7; }}
  .page-header {{ background: linear-gradient(135deg, #8e2de2 0%, #4a00e0 50%, #c0392b 100%); color: white; padding: 36px 24px; text-align: center; }}
  .page-header h1 {{ font-size: 1.7rem; margin-bottom: 6px; }}
  .page-header .subtitle {{ opacity: .9; font-size: .92rem; }}
  .container {{ max-width: 900px; margin: 0 auto; padding: 24px; }}
  .nav-back {{ display: inline-block; padding: 8px 16px; background: white; border-radius: 6px; text-decoration: none; color: #2d3748; box-shadow: 0 2px 4px rgba(0,0,0,.08); font-size: .88rem; margin-bottom: 20px; }}
  .intro {{ background: white; border-radius: 12px; padding: 18px 22px; box-shadow: 0 2px 6px rgba(0,0,0,.06); margin-bottom: 22px; font-size: .92rem; color: #4a5568; }}
  .intro h2 {{ font-size: 1rem; color: #4a00e0; margin-bottom: 8px; }}
  {extra_style}
</style>
</head>
<body>
<div class="page-header">
  <h1>EX 弱点強化ユニット</h1>
  <div class="subtitle">模擬試験の失点を挽回するための独立学習ユニット</div>
</div>
<div class="container">
  <a class="nav-back" href="mock_exam_report.html">← 結果レポート</a>
  <a class="nav-back" href="index.html" style="margin-left:8px">📚 教科書トップ</a>

  <div class="intro">
    <h2>🗂 このページについて</h2>
    各 <b>EX ユニット</b> は、模擬試験の弱点領域に対する独立した強化教材。D1〜D8 教科書とは別系統で、失点の多い順に EX1〜EX8 として並ぶ。優先度「最優先」の EX1／EX2 から着手し、試験直前は全ユニットを通読する想定。
  </div>

  <div class="ex-grid">{cards}
  </div>

  <div style="text-align:center;color:#a0aec0;font-size:.78rem;margin-top:30px;padding-top:16px;border-top:1px solid #e2e8f0">
    Phase 2 / 弱点強化ユニット索引
  </div>
</div>
</body>
</html>
"""


# Write files
for ex_id, dom, label, prio in EX_ORDER:
    block = blocks.get(dom)
    if block is None:
        print(f"WARN: missing block for {dom}")
        continue
    html = make_page(ex_id, dom, label, prio, block)
    for outdir in ["dist", "textbooks"]:
        out = ROOT / outdir / f"{ex_id}_reinforce.html"
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out}")

# Overwrite mock_exam_reinforce.html as EX index in both locations
ex_index = make_ex_index()
for outdir in ["dist", "textbooks"]:
    out = ROOT / outdir / "mock_exam_reinforce.html"
    out.write_text(ex_index, encoding="utf-8")
    print(f"wrote {out}")
