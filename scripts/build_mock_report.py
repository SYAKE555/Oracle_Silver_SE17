#!/usr/bin/env python3
"""Build mock_exam_report.html by embedding JSON data into a template."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "dist" / "mock_exam_data.json").read_text(encoding="utf-8"))

DOMAIN_META = {
    "D1": ("SQLとRDBの基礎", "D1_textbook.html"),
    "D2": ("データの絞り込みとソート", "D2_textbook.html"),
    "D3": ("単一行関数", "D3_textbook.html"),
    "D4": ("グループ関数と集計", "D4_textbook.html"),
    "D5": ("複数表の結合", "D5_textbook.html"),
    "D6": ("サブクエリ・集合演算", "D6_textbook.html"),
    "D7": ("DML・トランザクション", "D7_textbook.html"),
    "D8": ("DDL・オブジェクト管理", "D8_textbook.html"),
}

# Build aggregate summary combining both exams
combined = {d: {"total": 0, "correct": 0, "wrong": []} for d in DOMAIN_META}
per_exam_per_domain = {}
for exam in DATA["exams"]:
    eid = exam["exam_id"]
    per_exam_per_domain[eid] = {d: {"total": 0, "correct": 0, "wrong": [], "unclear": []} for d in DOMAIN_META}
    for q in exam["questions"]:
        d = q["domain"]
        if d not in combined:
            continue
        combined[d]["total"] += 1
        per_exam_per_domain[eid][d]["total"] += 1
        if q["correct"]:
            combined[d]["correct"] += 1
            per_exam_per_domain[eid][d]["correct"] += 1
        else:
            combined[d]["wrong"].append((eid, q["q"]))
            per_exam_per_domain[eid][d]["wrong"].append(q["q"])
        if q.get("unclear"):
            per_exam_per_domain[eid][d]["unclear"].append(q["q"])

# Weakness ranking by combined correct rate
weakness = []
for d, v in combined.items():
    pct = (v["correct"] / v["total"] * 100) if v["total"] else 100
    weakness.append((d, v["total"], v["correct"], pct))
weakness.sort(key=lambda x: x[3])  # ascending = weakest first

# Exam totals
exam_totals = []
for exam in DATA["exams"]:
    total_q = len(exam["questions"])
    correct_q = sum(1 for q in exam["questions"] if q["correct"])
    exam_totals.append({
        "id": exam["exam_id"],
        "score": exam["final_score"],
        "total_q": total_q,
        "correct_q": correct_q,
        "accuracy": (correct_q / total_q * 100) if total_q else 0,
    })

# Build HTML
def domain_bar_row(dom, total, correct, wrong_list=None):
    pct = (correct / total * 100) if total else 0
    name, link = DOMAIN_META[dom]
    bar_color = "#c0392b" if pct < 40 else ("#e67e22" if pct < 60 else ("#2ecc71" if pct >= 80 else "#f1c40f"))
    wrong_html = ""
    if wrong_list:
        if isinstance(wrong_list[0], tuple):
            labels = [f'<span class="q-tag">第{e}回 問{q}</span>' for e, q in wrong_list]
        else:
            labels = [f'<span class="q-tag">問{q}</span>' for q in wrong_list]
        wrong_html = f'<div class="wrong-list">{"".join(labels)}</div>'
    return f"""
    <div class="domain-row">
      <div class="domain-head">
        <a href="{link}" class="domain-name"><strong>{dom}</strong> {name}</a>
        <span class="domain-score">{correct}/{total} <b>({pct:.0f}%)</b></span>
      </div>
      <div class="bar-bg"><div class="bar-fg" style="width:{pct:.1f}%;background:{bar_color}"></div></div>
      {wrong_html}
    </div>
    """


def exam_card(e):
    acc = e["accuracy"]
    color = "#c0392b" if acc < 40 else ("#e67e22" if acc < 60 else "#2ecc71")
    return f"""
    <div class="exam-card">
      <div class="exam-title">第{e['id']}回 模擬試験</div>
      <div class="exam-score-big" style="color:{color}">{e['score']}<span class="unit">点</span></div>
      <div class="exam-sub">正答数 {e['correct_q']} / {e['total_q']}（正答率 {acc:.0f}%）</div>
    </div>
    """


# Per-exam domain tables
per_exam_html = ""
for exam in DATA["exams"]:
    eid = exam["exam_id"]
    rows = ""
    for d in sorted(DOMAIN_META.keys()):
        v = per_exam_per_domain[eid][d]
        if v["total"] == 0:
            continue
        rows += domain_bar_row(d, v["total"], v["correct"], v["wrong"])
    per_exam_html += f"""
    <div class="exam-section">
      <h3>第{eid}回 ドメイン別正答率</h3>
      {rows}
    </div>
    """

# Combined weakness list
weakness_html = ""
for idx, (d, total, correct, pct) in enumerate(weakness):
    name, link = DOMAIN_META[d]
    priority = "最優先" if idx < 2 else ("優先" if idx < 4 else "要復習" if pct < 70 else "維持")
    priority_class = "p-high" if idx < 2 else ("p-mid" if idx < 4 else "p-low" if pct < 70 else "p-ok")
    weakness_html += f"""
    <div class="weakness-item {priority_class}">
      <div class="rank">#{idx+1}</div>
      <div class="wk-main">
        <a href="{link}"><strong>{d}</strong> {name}</a>
        <div class="wk-sub">合計正答率 {pct:.0f}%（{correct}/{total}）</div>
      </div>
      <div class="priority">{priority}</div>
    </div>
    """

# Combined bar section
combined_bars = ""
for d in sorted(DOMAIN_META.keys()):
    v = combined[d]
    combined_bars += domain_bar_row(d, v["total"], v["correct"], v["wrong"])

# Unclear memo
unclear_html = ""
for exam in DATA["exams"]:
    u = [q["q"] for q in exam["questions"] if q.get("unclear")]
    if u:
        unclear_html += f'<li>第{exam["exam_id"]}回：{", ".join(f"問{q}" for q in u)}</li>'
if unclear_html:
    unclear_html = f'<div class="memo-box"><h4> 本人メモ「わかっていない問題」</h4><ul>{unclear_html}</ul></div>'

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>模擬試験 結果分析 - Oracle Silver SQL</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', 'Hiragino Sans', Arial, sans-serif; background: #f5f7fa; color: #2d3748; line-height: 1.6; }}
  .page-header {{ background: linear-gradient(135deg, #2c3e50 0%, #34495e 60%, #c0392b 100%); color: white; padding: 40px 24px; text-align: center; }}
  .page-header h1 {{ font-size: 1.8rem; margin-bottom: 6px; }}
  .page-header .subtitle {{ opacity: 0.9; font-size: 0.95rem; }}
  .container {{ max-width: 1100px; margin: 0 auto; padding: 24px; }}
  .nav-back {{ display: inline-block; padding: 8px 16px; background: white; border-radius: 6px; text-decoration: none; color: #2d3748; box-shadow: 0 2px 4px rgba(0,0,0,.08); font-size: .9rem; margin-bottom: 16px; }}
  .nav-back:hover {{ background: #edf2f7; }}

  .summary-row {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 24px; }}
  .exam-card {{ background: white; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,.08); text-align: center; }}
  .exam-title {{ font-size: 1rem; color: #4a5568; font-weight: 600; margin-bottom: 12px; }}
  .exam-score-big {{ font-size: 3.5rem; font-weight: 900; line-height: 1; }}
  .exam-score-big .unit {{ font-size: 1.2rem; font-weight: 500; margin-left: 4px; color: #718096; }}
  .exam-sub {{ margin-top: 8px; color: #718096; font-size: .9rem; }}

  .section-heading {{ font-size: 1.15rem; font-weight: 700; margin: 28px 0 14px; padding: 10px 14px; background: white; border-radius: 8px; border-left: 5px solid #c0392b; box-shadow: 0 2px 6px rgba(0,0,0,.06); }}
  .card {{ background: white; border-radius: 12px; padding: 20px 22px; box-shadow: 0 2px 8px rgba(0,0,0,.08); margin-bottom: 16px; }}

  .domain-row {{ margin-bottom: 14px; }}
  .domain-head {{ display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px; font-size: .95rem; }}
  .domain-name {{ color: #2d3748; text-decoration: none; }}
  .domain-name:hover {{ color: #c0392b; text-decoration: underline; }}
  .domain-score {{ color: #4a5568; font-size: .9rem; }}
  .bar-bg {{ background: #edf2f7; height: 14px; border-radius: 7px; overflow: hidden; }}
  .bar-fg {{ height: 100%; border-radius: 7px; transition: width .4s; }}
  .wrong-list {{ margin-top: 6px; }}
  .q-tag {{ display: inline-block; background: #fee; color: #c0392b; padding: 2px 8px; border-radius: 10px; font-size: .75rem; margin: 2px 3px 0 0; }}

  .exam-section {{ margin-bottom: 26px; }}
  .exam-section h3 {{ font-size: 1rem; color: #4a5568; margin-bottom: 10px; padding-bottom: 6px; border-bottom: 2px solid #e2e8f0; }}

  .weakness-grid {{ display: grid; gap: 10px; }}
  .weakness-item {{ display: grid; grid-template-columns: 50px 1fr auto; gap: 14px; align-items: center; padding: 12px 16px; border-radius: 8px; background: white; border-left: 4px solid #cbd5e0; }}
  .weakness-item.p-high {{ border-left-color: #c0392b; background: #fef5f5; }}
  .weakness-item.p-mid {{ border-left-color: #e67e22; background: #fef8f0; }}
  .weakness-item.p-low {{ border-left-color: #f1c40f; background: #fffbe8; }}
  .weakness-item.p-ok {{ border-left-color: #2ecc71; background: #f0fdf4; }}
  .rank {{ font-size: 1.3rem; font-weight: 900; color: #718096; }}
  .wk-main a {{ color: #2d3748; text-decoration: none; }}
  .wk-main a:hover {{ color: #c0392b; }}
  .wk-sub {{ font-size: .8rem; color: #718096; margin-top: 2px; }}
  .priority {{ font-weight: 700; font-size: .85rem; padding: 4px 10px; border-radius: 10px; background: #fff; color: #4a5568; white-space: nowrap; }}
  .p-high .priority {{ background: #c0392b; color: white; }}
  .p-mid .priority {{ background: #e67e22; color: white; }}
  .p-low .priority {{ background: #f1c40f; color: white; }}
  .p-ok .priority {{ background: #2ecc71; color: white; }}

  .memo-box {{ background: #fff8e1; border-left: 4px solid #f1c40f; padding: 14px 18px; border-radius: 8px; margin: 16px 0; }}
  .memo-box h4 {{ font-size: .95rem; color: #7c5a00; margin-bottom: 6px; }}
  .memo-box ul {{ list-style: none; font-size: .9rem; color: #5c4400; }}
  .memo-box li {{ padding: 2px 0; }}

  .tab-bar {{ display: flex; gap: 4px; margin-bottom: 14px; border-bottom: 2px solid #e2e8f0; }}
  .tab {{ padding: 10px 16px; background: transparent; border: none; cursor: pointer; font-weight: 600; color: #718096; border-bottom: 3px solid transparent; margin-bottom: -2px; }}
  .tab.active {{ color: #c0392b; border-bottom-color: #c0392b; }}
  .tab-content {{ display: none; }}
  .tab-content.active {{ display: block; }}

  .action-link {{ display: inline-block; margin-top: 14px; padding: 10px 18px; background: #c0392b; color: white; text-decoration: none; border-radius: 8px; font-weight: 600; font-size: .9rem; }}
  .action-link:hover {{ background: #a52f22; }}

  @media (max-width: 640px) {{
    .page-header h1 {{ font-size: 1.4rem; }}
    .exam-score-big {{ font-size: 2.8rem; }}
    .weakness-item {{ grid-template-columns: 40px 1fr auto; padding: 10px 12px; }}
  }}
</style>
</head>
<body>
<div class="page-header">
  <h1>模擬試験 結果分析レポート</h1>
  <div class="subtitle">Oracle Master Silver SQL (1Z0-071) - 失点分析と強化ポイント</div>
</div>
<div class="container">
  <a class="nav-back" href="index.html">← 教科書トップへ戻る</a>

  <div class="section-heading"> 総合スコア</div>
  <div class="summary-row">
    {"".join(exam_card(e) for e in exam_totals)}
    <div class="exam-card">
      <div class="exam-title">合計正答率の推移</div>
      <div style="font-size:1.8rem;font-weight:700;margin-top:12px">{exam_totals[0]['accuracy']:.0f}%  {exam_totals[1]['accuracy']:.0f}%</div>
      <div class="exam-sub">第1回  第2回</div>
      <div style="margin-top:10px;font-size:.85rem;color:#c0392b;font-weight:600">
        {' 下降傾向 — 復習優先度を上げる' if exam_totals[1]['accuracy'] < exam_totals[0]['accuracy'] else ' 改善傾向'}
      </div>
    </div>
  </div>

  {unclear_html}

  <div class="section-heading"> 弱点ランキング（2回合計ベース）</div>
  <div class="card">
    <p style="font-size:.85rem;color:#4a5568;margin-bottom:12px">正答率の低い順にドメインをランキング。<b>最優先</b>と<b>優先</b>の4領域を重点的に復習する。</p>
    <div class="weakness-grid">
      {weakness_html}
    </div>
    <a href="mock_exam_reinforce.html" class="action-link"> 弱点強化学習ページへ（Phase 2）</a>
  </div>

  <div class="section-heading"> ドメイン別・詳細分析</div>
  <div class="card">
    <div class="tab-bar">
      <button class="tab active" onclick="showTab('combined')">合計</button>
      <button class="tab" onclick="showTab('exam1')">第1回</button>
      <button class="tab" onclick="showTab('exam2')">第2回</button>
    </div>
    <div id="tab-combined" class="tab-content active">
      {combined_bars}
    </div>
    <div id="tab-exam1" class="tab-content">
      {"".join(domain_bar_row(d, per_exam_per_domain[1][d]['total'], per_exam_per_domain[1][d]['correct'], per_exam_per_domain[1][d]['wrong']) for d in sorted(DOMAIN_META.keys()) if per_exam_per_domain[1][d]['total']>0)}
    </div>
    <div id="tab-exam2" class="tab-content">
      {"".join(domain_bar_row(d, per_exam_per_domain[2][d]['total'], per_exam_per_domain[2][d]['correct'], per_exam_per_domain[2][d]['wrong']) for d in sorted(DOMAIN_META.keys()) if per_exam_per_domain[2][d]['total']>0)}
    </div>
  </div>

  <div class="section-heading"> 所感と次アクション</div>
  <div class="card">
    <ul style="padding-left: 20px; font-size: .92rem; color: #2d3748;">
      <li style="margin-bottom:8px"><b>最優先復習領域：</b>正答率40%未満のドメインは、教科書D章 + 関連DBA章を読み直した上で、該当問題を改めて解く。</li>
      <li style="margin-bottom:8px"><b>設問タイプの弱点：</b>複数選択問題（「2つ選択」「3つ選択」）での取りこぼしが多い場合、すべての選択肢を個別に○×判定する癖をつける。</li>
      <li style="margin-bottom:8px"><b>構文の細部：</b>エイリアスの引用符、LIKE のワイルドカード位置、NULL 比較演算子（= NULL は使えない）など、細部を機械的に暗記する領域を洗い出す。</li>
      <li><b>Phase 2：</b>弱点強化ページで各ドメインの典型ミスパターンと必修構文を集中特訓する。</li>
    </ul>
  </div>

  <div style="text-align:center;color:#a0aec0;font-size:.8rem;margin-top:40px;padding-top:20px;border-top:1px solid #e2e8f0">
    自動生成: scripts/build_mock_report.py（データ: dist/mock_exam_data.json）
  </div>
</div>

<script>
function showTab(name) {{
  document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach(c=>c.classList.remove('active'));
  event.target.classList.add('active');
  document.getElementById('tab-'+name).classList.add('active');
}}
</script>
</body>
</html>
"""

out = ROOT / "dist" / "mock_exam_report.html"
out.write_text(HTML, encoding="utf-8")
print(f"Wrote {out}")

# Also copy to textbooks/
textbook_out = ROOT / "textbooks" / "mock_exam_report.html"
textbook_out.write_text(HTML, encoding="utf-8")
data_out = ROOT / "textbooks" / "mock_exam_data.json"
data_out.write_text((ROOT / "dist" / "mock_exam_data.json").read_text(encoding="utf-8"), encoding="utf-8")
print(f"Wrote {textbook_out}")
