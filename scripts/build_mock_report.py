#!/usr/bin/env python3
"""Build mock_exam_report.html by embedding JSON data into a static template."""
from __future__ import annotations

import html
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

EXAMS = sorted(DATA["exams"], key=lambda exam: exam["exam_id"])
BY_EXAM = DATA["summary"]["by_exam"]
COMBINED = DATA["summary"]["combined"]
OVERALL = DATA["summary"]["overall"]


def pct(value: int, total: int) -> float:
    return (value / total * 100.0) if total else 0.0


def color_for_pct(value: float) -> str:
    if value < 40:
        return "#c0392b"
    if value < 60:
        return "#e67e22"
    if value < 75:
        return "#f1c40f"
    return "#2ecc71"


def priority_for_rank(rank: int, accuracy: float) -> tuple[str, str]:
    if rank < 2:
        return "最優先", "p-high"
    if rank < 5:
        return "優先", "p-mid"
    if accuracy < 75:
        return "要復習", "p-low"
    return "維持", "p-ok"


def trend_text(delta: float) -> str:
    if delta >= 10:
        return f"{delta:+.0f}pt 改善"
    if delta <= -10:
        return f"{delta:+.0f}pt 低下"
    return f"{delta:+.0f}pt 横ばい"


def trend_class(delta: float) -> str:
    if delta >= 10:
        return "up"
    if delta <= -10:
        return "down"
    return "flat"


def exam_link_label(exam_id: int, qnum: int) -> str:
    return f"第{exam_id}回 問{qnum}"


def wrong_tags(items: list[dict] | list[int], with_exam: bool) -> str:
    if not items:
        return ""
    labels = []
    if with_exam:
        for item in items:
            labels.append(f'<span class="q-tag">{exam_link_label(item["exam_id"], item["q"])}</span>')
    else:
        for qnum in items:
            labels.append(f'<span class="q-tag">問{qnum}</span>')
    return f'<div class="wrong-list">{"".join(labels)}</div>'


def domain_row(domain: str, total: int, correct: int, wrong_items: list, with_exam: bool) -> str:
    name, link = DOMAIN_META[domain]
    accuracy = pct(correct, total)
    return f"""
    <div class="domain-row">
      <div class="domain-head">
        <a href="{link}" class="domain-name"><strong>{domain}</strong> {name}</a>
        <span class="domain-score">{correct}/{total} <b>({accuracy:.0f}%)</b></span>
      </div>
      <div class="bar-bg"><div class="bar-fg" style="width:{accuracy:.1f}%;background:{color_for_pct(accuracy)}"></div></div>
      {wrong_tags(wrong_items, with_exam)}
    </div>
    """


domain_rank_data = []
total_wrong_questions = max(OVERALL["wrong_questions"], 1)
for domain in DOMAIN_META:
    combined = COMBINED[domain]
    rates = []
    for exam in EXAMS:
        stats = BY_EXAM[f"exam{exam['exam_id']}"][domain]
        rates.append(stats["accuracy"] if stats["total"] else None)
    non_null_rates = [rate for rate in rates if rate is not None]
    first_rate = non_null_rates[0] if non_null_rates else 0.0
    latest_rate = non_null_rates[-1] if non_null_rates else 0.0
    delta = latest_rate - first_rate
    question_share = pct(combined["total"], OVERALL["question_count"])
    miss_share = pct(len(combined["wrong"]), total_wrong_questions)
    domain_rank_data.append(
        {
            "domain": domain,
            "name": DOMAIN_META[domain][0],
            "link": DOMAIN_META[domain][1],
            "total": combined["total"],
            "correct": combined["correct"],
            "accuracy": combined["accuracy"],
            "rates": rates,
            "latest_rate": latest_rate,
            "delta": delta,
            "question_share": question_share,
            "miss_share": miss_share,
            "wrong": combined["wrong"],
        }
    )

domain_rank_data.sort(key=lambda item: (item["accuracy"], -item["miss_share"], item["domain"]))
for index, item in enumerate(domain_rank_data):
    priority_label, priority_class = priority_for_rank(index, item["accuracy"])
    item["rank"] = index + 1
    item["priority_label"] = priority_label
    item["priority_class"] = priority_class

best_exam = max(EXAMS, key=lambda exam: exam["final_score"])
latest_exam = EXAMS[-1]
top_strengths = sorted(domain_rank_data, key=lambda item: (-item["accuracy"], -item["delta"], item["domain"]))[:3]
top_gaps = domain_rank_data[:4]
top_miss = max(domain_rank_data, key=lambda item: item["miss_share"])


def exam_card(exam: dict) -> str:
    score_color = color_for_pct(exam["score_ratio"])
    accuracy_color = color_for_pct(exam["accuracy"])
    return f"""
    <div class="exam-card">
      <div class="exam-title">{html.escape(exam["title"])}</div>
      <div class="score-line">
        <span class="score-value" style="color:{score_color}">{exam["final_score"]}</span>
        <span class="score-unit">/ 100</span>
      </div>
      <div class="score-meta">得点比率 {exam["score_ratio"]:.0f}%</div>
      <div class="mini-metric">
        <span>正答率</span>
        <b style="color:{accuracy_color}">{exam["accuracy"]:.0f}%</b>
      </div>
      <div class="mini-metric">
        <span>正答数</span>
        <b>{exam["correct_questions"]} / {exam["total_questions"]}</b>
      </div>
      <div class="mini-metric">
        <span>失点数</span>
        <b>{exam["wrong_questions"]}</b>
      </div>
    </div>
    """


def domain_panel(item: dict) -> str:
    trend_boxes = []
    for rate, exam in zip(item["rates"], EXAMS):
        label = "未出題" if rate is None else f"{rate:.0f}%"
        cls = "dim" if rate is None else ""
        trend_boxes.append(f'<div class="trend-box {cls}"><span>第{exam["exam_id"]}回</span><b>{label}</b></div>')

    if item["accuracy"] >= 70:
        good_point = "評価: 正答率が高く、試験直前の確認で維持できる。"
    elif item["delta"] >= 10:
        good_point = "評価: 直近で持ち直しており、復習の効果が見えている。"
    else:
        good_point = "評価: 基礎理解は残っているため、典型問題の再演習で戻しやすい。"

    if item["accuracy"] < 40:
        weak_point = "補強: 用語暗記だけでなく、構文パターンをまとめて再インストールする。"
    elif item["miss_share"] >= 15:
        weak_point = "補強: 全体失点への影響が大きく、優先的に取り返す必要がある。"
    else:
        weak_point = "補強: 失点パターンを絞って、確認テストで再発を止める。"

    return f"""
    <div class="progress-card {item['priority_class']}">
      <div class="progress-head">
        <div>
          <a href="{item['link']}" class="progress-title"><strong>{item['domain']}</strong> {item['name']}</a>
          <div class="progress-sub">出題比率 {item['question_share']:.0f}% / 失点比率 {item['miss_share']:.0f}%</div>
        </div>
        <div class="priority-pill">{item['priority_label']}</div>
      </div>
      <div class="meter-label"><span>進捗率</span><b>{item['accuracy']:.0f}%</b></div>
      <div class="bar-bg"><div class="bar-fg" style="width:{item['accuracy']:.1f}%;background:{color_for_pct(item['accuracy'])}"></div></div>
      <div class="meter-label"><span>全体失点への影響</span><b>{item['miss_share']:.0f}%</b></div>
      <div class="bar-bg bar-bg-loss"><div class="bar-fg" style="width:{item['miss_share']:.1f}%;background:#2c3e50"></div></div>
      <div class="trend-strip">
        {''.join(trend_boxes)}
      </div>
      <div class="delta-chip {trend_class(item['delta'])}">{trend_text(item['delta'])}</div>
      <p class="progress-note">{good_point}</p>
      <p class="progress-note weak">{weak_point}</p>
    </div>
    """


strengths_html = "".join(
    f"""
    <li>
      <a href="{item['link']}"><strong>{item['domain']}</strong> {item['name']}</a>
      <span>進捗 {item['accuracy']:.0f}% / 直近 {item['latest_rate']:.0f}%</span>
    </li>
    """
    for item in top_strengths
)

gaps_html = "".join(
    f"""
    <li>
      <a href="{item['link']}"><strong>{item['domain']}</strong> {item['name']}</a>
      <span>進捗 {item['accuracy']:.0f}% / 失点比率 {item['miss_share']:.0f}%</span>
    </li>
    """
    for item in top_gaps
)

unclear_items = []
for exam in EXAMS:
    if exam["memo"]:
        joined = " / ".join(f"問{number}" for number in exam["memo"])
        unclear_items.append(f"<li>{html.escape(exam['title'])}: {joined}</li>")
unclear_html = ""
if unclear_items:
    unclear_html = f'<div class="memo-box"><h4>本人メモ「まだ曖昧な問題」</h4><ul>{"".join(unclear_items)}</ul></div>'

combined_rows = "".join(
    domain_row(item["domain"], item["total"], item["correct"], item["wrong"], True)
    for item in domain_rank_data
)

per_exam_tabs = []
tab_buttons = ['<button class="tab active" onclick="showTab(event, \'combined\')">合計</button>']
tab_contents = [f'<div id="tab-combined" class="tab-content active">{combined_rows}</div>']
for exam in EXAMS:
    tab_name = f"exam{exam['exam_id']}"
    tab_buttons.append(
        f'<button class="tab" onclick="showTab(event, \'{tab_name}\')">第{exam["exam_id"]}回</button>'
    )
    rows = []
    for domain in DOMAIN_META:
        values = BY_EXAM[f"exam{exam['exam_id']}"][domain]
        if values["total"] == 0:
            continue
        rows.append(domain_row(domain, values["total"], values["correct"], values["wrong"], False))
    tab_contents.append(f'<div id="tab-{tab_name}" class="tab-content">{"".join(rows)}</div>')

phase_items = [
    f"<li><b>Phase 1:</b> 結果レポートで {top_miss['domain']} と {top_gaps[1]['domain']} の失点比率を確認し、失点の大きい順に手を付ける。</li>",
    f"<li><b>Phase 2:</b> 強化学習ページでは {top_gaps[0]['domain']} から {top_gaps[min(2, len(top_gaps) - 1)]['domain']} までを優先し、類題を繰り返す。</li>",
    "<li><b>Phase 3:</b> 直近模試で正答率が50%を下回った領域は、教科書の該当章を要点ごとに再暗記してから再挑戦する。</li>",
]

HTML = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>模擬試験 結果分析 - Oracle Silver SQL</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Noto Sans JP', 'Hiragino Sans', sans-serif; background: #edf2f7; color: #1f2937; line-height: 1.7; }}
  a {{ color: inherit; }}
  .page-header {{ background: linear-gradient(135deg, #132238 0%, #1d3557 58%, #c0392b 100%); color: white; padding: 46px 24px; text-align: center; }}
  .page-header h1 {{ font-size: 2rem; margin-bottom: 8px; }}
  .page-header .subtitle {{ opacity: 0.92; font-size: 0.96rem; }}
  .container {{ max-width: 1180px; margin: 0 auto; padding: 24px; }}
  .nav-back {{ display: inline-block; padding: 8px 16px; background: white; border-radius: 999px; text-decoration: none; color: #1f2937; box-shadow: 0 4px 16px rgba(15, 23, 42, 0.08); font-size: 0.9rem; margin-bottom: 18px; }}
  .nav-back:hover {{ background: #f8fafc; }}

  .section-heading {{ font-size: 1.15rem; font-weight: 800; margin: 26px 0 14px; padding: 12px 16px; background: white; border-radius: 12px; border-left: 6px solid #c0392b; box-shadow: 0 6px 18px rgba(15, 23, 42, 0.07); }}
  .section-copy {{ color: #475569; font-size: 0.92rem; margin-bottom: 12px; padding: 0 2px; }}
  .card {{ background: white; border-radius: 18px; padding: 22px; box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08); margin-bottom: 16px; }}

  .summary-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; }}
  .exam-card {{ background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); border: 1px solid #e2e8f0; border-radius: 18px; padding: 22px; box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06); }}
  .exam-title {{ font-size: 0.95rem; color: #475569; font-weight: 700; margin-bottom: 10px; }}
  .score-line {{ display: flex; align-items: baseline; gap: 6px; }}
  .score-value {{ font-size: 3rem; font-weight: 900; line-height: 1; }}
  .score-unit {{ font-size: 1rem; color: #64748b; font-weight: 700; }}
  .score-meta {{ margin-top: 6px; color: #334155; font-size: 0.92rem; font-weight: 700; }}
  .mini-metric {{ display: flex; justify-content: space-between; gap: 10px; font-size: 0.88rem; color: #475569; padding-top: 10px; margin-top: 10px; border-top: 1px solid #e2e8f0; }}
  .mini-metric b {{ color: #0f172a; }}
  .overview-card {{ background: linear-gradient(160deg, #132238 0%, #1d3557 55%, #274c77 100%); color: white; }}
  .overview-card .exam-title, .overview-card .mini-metric, .overview-card .score-meta {{ color: rgba(255,255,255,0.88); }}
  .overview-card .mini-metric b {{ color: white; }}

  .memo-box {{ background: #fff8e1; border-left: 4px solid #f1c40f; padding: 16px 18px; border-radius: 12px; margin: 16px 0 4px; }}
  .memo-box h4 {{ font-size: 0.95rem; color: #7c5a00; margin-bottom: 6px; }}
  .memo-box ul {{ list-style: none; font-size: 0.92rem; color: #5c4400; }}
  .memo-box li {{ padding: 2px 0; }}

  .insight-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }}
  .insight-card h3 {{ font-size: 1rem; margin-bottom: 10px; }}
  .insight-card ul {{ list-style: none; display: grid; gap: 8px; }}
  .insight-card li {{ display: flex; justify-content: space-between; gap: 10px; padding: 10px 12px; background: #f8fafc; border-radius: 12px; font-size: 0.9rem; }}
  .insight-card li span {{ color: #475569; text-align: right; }}
  .insight-card a {{ text-decoration: none; }}
  .insight-card a:hover {{ color: #c0392b; }}
  .insight-card.good h3 {{ color: #166534; }}
  .insight-card.good li {{ border-left: 4px solid #22c55e; }}
  .insight-card.gap h3 {{ color: #991b1b; }}
  .insight-card.gap li {{ border-left: 4px solid #c0392b; }}

  .progress-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; }}
  .progress-card {{ border: 1px solid #e2e8f0; border-radius: 18px; padding: 18px; background: white; box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05); }}
  .progress-card.p-high {{ border-top: 5px solid #c0392b; }}
  .progress-card.p-mid {{ border-top: 5px solid #e67e22; }}
  .progress-card.p-low {{ border-top: 5px solid #f1c40f; }}
  .progress-card.p-ok {{ border-top: 5px solid #2ecc71; }}
  .progress-head {{ display: flex; justify-content: space-between; gap: 10px; align-items: start; margin-bottom: 12px; }}
  .progress-title {{ font-size: 1rem; font-weight: 800; text-decoration: none; }}
  .progress-title:hover {{ color: #c0392b; }}
  .progress-sub {{ color: #64748b; font-size: 0.82rem; margin-top: 4px; }}
  .priority-pill {{ padding: 6px 10px; border-radius: 999px; font-size: 0.78rem; font-weight: 800; white-space: nowrap; background: #0f172a; color: white; }}
  .meter-label {{ display: flex; justify-content: space-between; gap: 10px; font-size: 0.86rem; color: #475569; margin: 10px 0 6px; }}
  .bar-bg {{ background: #e2e8f0; height: 14px; border-radius: 999px; overflow: hidden; }}
  .bar-bg-loss {{ background: #dbe4ef; }}
  .bar-fg {{ height: 100%; border-radius: 999px; transition: width .35s ease; }}
  .trend-strip {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; margin-top: 14px; }}
  .trend-box {{ background: #f8fafc; border-radius: 12px; padding: 10px 8px; text-align: center; }}
  .trend-box span {{ display: block; color: #64748b; font-size: 0.78rem; margin-bottom: 4px; }}
  .trend-box b {{ font-size: 0.95rem; color: #0f172a; }}
  .trend-box.dim b {{ color: #94a3b8; }}
  .delta-chip {{ display: inline-block; margin-top: 12px; padding: 6px 10px; border-radius: 999px; font-size: 0.78rem; font-weight: 800; }}
  .delta-chip.up {{ background: #dcfce7; color: #166534; }}
  .delta-chip.down {{ background: #fee2e2; color: #991b1b; }}
  .delta-chip.flat {{ background: #e2e8f0; color: #334155; }}
  .progress-note {{ margin-top: 10px; font-size: 0.88rem; color: #334155; }}
  .progress-note.weak {{ color: #7f1d1d; }}

  .domain-row {{ margin-bottom: 16px; }}
  .domain-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 12px; margin-bottom: 5px; font-size: 0.95rem; }}
  .domain-name {{ color: #1f2937; text-decoration: none; }}
  .domain-name:hover {{ color: #c0392b; text-decoration: underline; }}
  .domain-score {{ color: #475569; font-size: 0.9rem; white-space: nowrap; }}
  .wrong-list {{ margin-top: 7px; }}
  .q-tag {{ display: inline-block; background: #fef2f2; color: #b91c1c; padding: 3px 8px; border-radius: 999px; font-size: 0.76rem; margin: 2px 4px 0 0; }}

  .tab-bar {{ display: flex; gap: 4px; margin-bottom: 14px; border-bottom: 2px solid #e2e8f0; overflow-x: auto; }}
  .tab {{ padding: 10px 16px; background: transparent; border: none; cursor: pointer; font-weight: 700; color: #64748b; border-bottom: 3px solid transparent; margin-bottom: -2px; white-space: nowrap; }}
  .tab.active {{ color: #c0392b; border-bottom-color: #c0392b; }}
  .tab-content {{ display: none; }}
  .tab-content.active {{ display: block; }}

  .phase-list {{ padding-left: 20px; color: #334155; font-size: 0.92rem; }}
  .phase-list li {{ margin-bottom: 10px; }}

  .action-link {{ display: inline-block; margin-top: 14px; padding: 11px 18px; background: #c0392b; color: white; text-decoration: none; border-radius: 999px; font-weight: 700; font-size: 0.9rem; }}
  .action-link:hover {{ background: #a52f22; }}

  @media (max-width: 720px) {{
    .page-header h1 {{ font-size: 1.55rem; }}
    .container {{ padding: 18px; }}
    .score-value {{ font-size: 2.5rem; }}
    .progress-head, .domain-head {{ flex-direction: column; align-items: start; }}
    .trend-strip {{ grid-template-columns: 1fr; }}
  }}
</style>
</head>
<body>
<div class="page-header">
  <h1>模擬試験 結果分析レポート</h1>
  <div class="subtitle">3回分の模擬試験結果から、失点の集中領域と補強優先度を整理した進捗レポート</div>
</div>
<div class="container">
  <a class="nav-back" href="index.html">教科書トップへ戻る</a>

  <div class="section-heading">総合スコア</div>
  <p class="section-copy">得点比率は模試スコア、進捗率は設問ベースの正答率です。どちらも並べて見ることで、点数の推移と知識定着の両方を把握できます。</p>
  <div class="summary-grid">
    {''.join(exam_card(exam) for exam in EXAMS)}
    <div class="exam-card overview-card">
      <div class="exam-title">全体サマリー</div>
      <div class="score-line">
        <span class="score-value" style="color:#ffffff">{OVERALL["average_score"]:.1f}</span>
        <span class="score-unit">平均点</span>
      </div>
      <div class="score-meta">平均得点比率 {OVERALL["average_score_ratio"]:.1f}% / 平均進捗率 {OVERALL["accuracy"]:.0f}%</div>
      <div class="mini-metric"><span>最高得点</span><b>{best_exam["title"]} {best_exam["final_score"]}点</b></div>
      <div class="mini-metric"><span>直近結果</span><b>{latest_exam["title"]} {latest_exam["final_score"]}点</b></div>
      <div class="mini-metric"><span>最大失点領域</span><b>{top_miss["domain"]} {top_miss["miss_share"]:.0f}%</b></div>
    </div>
  </div>

  {unclear_html}

  <div class="section-heading">評価できる点と抜けている点</div>
  <div class="insight-grid">
    <div class="card insight-card good">
      <h3>評価できる点</h3>
      <ul>
        {strengths_html}
      </ul>
    </div>
    <div class="card insight-card gap">
      <h3>抜けが残る点</h3>
      <ul>
        {gaps_html}
      </ul>
    </div>
  </div>

  <div class="section-heading">ドメイン別進捗ボード</div>
  <p class="section-copy">各項目ごとに、進捗率・全体失点への影響・試験ごとの変動を可視化しています。優先度の高い順に並べています。</p>
  <div class="progress-grid">
    {''.join(domain_panel(item) for item in domain_rank_data)}
  </div>

  <div class="section-heading">弱点ランキングと詳細</div>
  <div class="card">
    <div class="tab-bar">
      {''.join(tab_buttons)}
    </div>
    {''.join(tab_contents)}
    <a href="mock_exam_reinforce.html" class="action-link">Phase 2 の強化学習ページへ</a>
  </div>

  <div class="section-heading">学習フェーズ方針</div>
  <div class="card">
    <ul class="phase-list">
      {''.join(phase_items)}
    </ul>
  </div>

  <div style="text-align:center;color:#94a3b8;font-size:0.8rem;margin-top:36px;padding-top:20px;border-top:1px solid #dbe4ef">
    自動生成: scripts/build_mock_report.py / データ: dist/mock_exam_data.json
  </div>
</div>

<script>
function showTab(event, name) {{
  document.querySelectorAll('.tab').forEach((tab) => tab.classList.remove('active'));
  document.querySelectorAll('.tab-content').forEach((content) => content.classList.remove('active'));
  event.currentTarget.classList.add('active');
  document.getElementById('tab-' + name).classList.add('active');
}}
</script>
</body>
</html>
"""

out = ROOT / "dist" / "mock_exam_report.html"
out.write_text(HTML, encoding="utf-8")
print(f"Wrote {out}")

textbook_out = ROOT / "textbooks" / "mock_exam_report.html"
textbook_out.write_text(HTML, encoding="utf-8")
data_out = ROOT / "textbooks" / "mock_exam_data.json"
data_out.write_text((ROOT / "dist" / "mock_exam_data.json").read_text(encoding="utf-8"), encoding="utf-8")
print(f"Wrote {textbook_out}")
