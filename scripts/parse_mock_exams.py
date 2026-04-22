#!/usr/bin/env python3
"""Parse mock exam text files into structured JSON for analysis."""
import re
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXAMS = [
    (ROOT / "模擬問題一回目　記録　48点.txt", 1, 48),
    (ROOT / "模擬問題二回目　記録　33点.txt", 2, 33),
]

# Keyword-based domain classifier mapping to D1-D8
# D1: SQL/RDB basics, SELECT basics, NULL
# D2: WHERE, LIKE, ORDER BY, row limit, substitution vars
# D3: single-row functions (文字/数値/日付/NULL関数/CASE/DECODE)
# D4: group functions, GROUP BY, HAVING
# D5: joins (INNER/OUTER/CROSS/自己結合/NATURAL)
# D6: subqueries, EXISTS, UNION/INTERSECT/MINUS
# D7: DML (INSERT/UPDATE/DELETE/MERGE/TRUNCATE/transactions)
# D8: DDL (CREATE TABLE/VIEW/SEQUENCE/INDEX/権限/ロール/SYNONYM/辞書)

DOMAIN_KEYWORDS = {
    "D1": ["リレーショナル", "主キー", "外部キー", "一意キー", "ERD", "正規化",
           "DDL", "DML", "DCL", "TCL", "オブジェクト型", "NULL値を持たせ",
           "DUAL", "スキーマ", "データベース管理"],
    "D2": ["LIKE", "ワイルドカード", "ORDER BY", "ROWNUM", "FETCH", "OFFSET",
           "置換変数", "VERIFY", "BETWEEN", "WHERE", " IN ", "比較演算子",
           "ASC", "DESC", "NULLS FIRST", "NULLS LAST"],
    "D3": ["UPPER", "LOWER", "INITCAP", "SUBSTR", "INSTR", "LENGTH", "LPAD",
           "RPAD", "TRIM", "REPLACE", "CONCAT", "ROUND", "TRUNC", "MOD",
           "SYSDATE", "CURRENT_DATE", "MONTHS_BETWEEN", "ADD_MONTHS",
           "NEXT_DAY", "LAST_DAY", "EXTRACT", "TO_CHAR", "TO_DATE",
           "TO_NUMBER", "NVL", "NVL2", "NULLIF", "COALESCE", "CASE", "DECODE",
           "暗黙的", "単一行関数"],
    "D4": ["GROUP BY", "HAVING", "SUM(", "AVG(", "MAX(", "MIN(", "COUNT(",
           "グループ関数", "集計", "ROLLUP", "CUBE"],
    "D5": ["JOIN", "INNER", "OUTER", "CROSS", "NATURAL", "USING", " ON ",
           "結合", "自己結合", "デカルト"],
    "D6": ["サブクエリ", "副問合せ", "EXISTS", "NOT EXISTS", "UNION",
           "INTERSECT", "MINUS", "ANY", " ALL ", "相関"],
    "D7": ["INSERT", "UPDATE", "DELETE", "MERGE", "TRUNCATE", "COMMIT",
           "ROLLBACK", "SAVEPOINT", "トランザクション", "マルチテーブル",
           "行レベルロック"],
    "D8": ["CREATE TABLE", "ALTER TABLE", "DROP TABLE", "VIEW", "SEQUENCE",
           "INDEX", "SYNONYM", "GRANT", "REVOKE", "ROLE", "権限", "ロール",
           "制約", "CHECK", "NOT NULL", "UNIQUE", "PRIMARY KEY",
           "FOREIGN KEY", "辞書", "ディクショナリ", "TIMESTAMP", "INTERVAL",
           "タイムゾーン", "WITH TIME ZONE"],
}


def classify(text: str) -> str:
    """Context-aware classifier returning best-matching domain."""
    upper = text.upper()

    # Hard rules (priority order)
    # DDL context: CREATE/ALTER/DROP of TABLE/VIEW/SEQUENCE/INDEX/SYNONYM
    ddl_context = any(kw in upper for kw in [
        "CREATE TABLE", "ALTER TABLE", "DROP TABLE",
        "CREATE VIEW", "DROP VIEW", "CREATE OR REPLACE VIEW",
        "CREATE SEQUENCE", "ALTER SEQUENCE", "CREATE INDEX",
        "CREATE SYNONYM", "GRANT ", "REVOKE ", "ロール",
        "CREATE USER", "CREATE ROLE", "データ・ディクショナリ",
        "USER_TABLES", "USER_CONSTRAINTS", "USER_TAB_COLUMNS",
        "ALL_TABLES", "DBA_TABLES", "TIMESTAMP WITH", "INTERVAL ",
        "タイムゾーン", "WITH TIME ZONE", "シノニム", "シーケンス",
        "ビュー", "READ ONLY", "CHECK OPTION",
    ])
    # 制約 only if in DDL context
    if "制約" in text and ddl_context:
        return "D8"
    if ddl_context:
        return "D8"

    # DML context
    dml_kws = ["INSERT INTO", "INSERT ALL", "INSERT FIRST", "UPDATE ",
               "DELETE FROM", "MERGE INTO", "TRUNCATE TABLE", "COMMIT",
               "ROLLBACK", "SAVEPOINT", "トランザクション", "マルチテーブル"]
    if any(kw in upper for kw in dml_kws):
        return "D7"

    # Set operators / subqueries
    set_ops = ["UNION ALL", "UNION", "INTERSECT", "MINUS",
               "EXISTS", "サブクエリ", "副問合せ", "相関"]
    if any(kw in upper for kw in set_ops):
        return "D6"
    # ANY/ALL with comparison — subquery
    if re.search(r"=\s*(ANY|ALL|SOME)\b", upper) or re.search(r"<\s*ANY\b|>\s*ANY\b", upper):
        return "D6"

    # Joins
    join_kws = ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN",
                "CROSS JOIN", "NATURAL JOIN", "OUTER JOIN", "USING (",
                "JOIN ", "自己結合", "デカルト"]
    if any(kw in upper for kw in join_kws):
        return "D5"

    # Group functions / aggregation
    if any(kw in upper for kw in ["GROUP BY", "HAVING", "ROLLUP", "CUBE"]):
        return "D4"
    if re.search(r"\b(SUM|AVG|COUNT|MAX|MIN)\s*\(", upper) and "GROUP" in upper:
        return "D4"

    # Single-row functions
    d3_fns = ["UPPER(", "LOWER(", "INITCAP(", "SUBSTR(", "INSTR(", "LENGTH(",
              "LPAD(", "RPAD(", "TRIM(", "REPLACE(", "CONCAT(",
              "ROUND(", "TRUNC(", "MOD(", "CEIL(", "FLOOR(",
              "SYSDATE", "CURRENT_DATE", "MONTHS_BETWEEN(", "ADD_MONTHS(",
              "NEXT_DAY(", "LAST_DAY(", "EXTRACT(",
              "TO_CHAR(", "TO_DATE(", "TO_NUMBER(",
              "NVL(", "NVL2(", "NULLIF(", "COALESCE(",
              "CASE ", "DECODE(", "単一行関数", "暗黙的"]
    if any(kw in upper for kw in d3_fns):
        return "D3"

    # Filtering / sorting / pagination
    d2_kws = ["LIKE", "ワイルドカード", "ORDER BY", "ROWNUM", "FETCH FIRST",
              "OFFSET", "置換変数", "VERIFY", "BETWEEN", " IN (",
              "NULLS FIRST", "NULLS LAST", "IS NULL", "IS NOT NULL",
              "WHERE "]
    if any(kw in upper for kw in d2_kws):
        return "D2"

    # D1 fallback (relational basics / SELECT basics)
    return "D1"


Q_HEADER = re.compile(r"^問題(\d+)\s*第\d+問目\s*/\s*全78問")
ANS_LINE = re.compile(r"^Ans\.(.*)$")
SELFANS_LINE = re.compile(r"^SelfAns\.(.*)$")
MARK_LINE = re.compile(r"^[○×]\s*$")


def parse_exam(path: Path, exam_id: int, final_score: int):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # memo: ちょっとわかってないメモ lines like ・問20
    memo = []
    for line in lines[:30]:
        m = re.match(r"^・問(\d+)", line.strip())
        if m:
            memo.append(int(m.group(1)))

    questions = []
    i = 0
    while i < len(lines):
        m = Q_HEADER.match(lines[i].strip())
        if not m:
            i += 1
            continue
        qnum = int(m.group(1))
        # collect until next Q_HEADER
        body = []
        j = i + 1
        while j < len(lines) and not Q_HEADER.match(lines[j].strip()):
            body.append(lines[j])
            j += 1
        # Parse body
        ans = None
        self_ans = None
        mark = None  # "○" or "×"
        q_text_lines = []
        for b in body:
            a = ANS_LINE.match(b.strip())
            s = SELFANS_LINE.match(b.strip())
            if a:
                ans = a.group(1).strip()
                continue
            if s:
                self_ans = s.group(1).strip()
                continue
            if MARK_LINE.match(b):
                mark = b.strip()
                continue
            q_text_lines.append(b)
        q_text = "\n".join(q_text_lines).strip()
        if mark is None:
            # If no mark but SelfAns missing and Ans present, assume correct
            mark = "○" if ans and self_ans is None else "×" if self_ans else "?"
        correct = (mark == "○")
        domain = classify(q_text + " " + (ans or ""))
        questions.append({
            "exam": exam_id,
            "q": qnum,
            "text": q_text[:500],
            "ans": ans,
            "self_ans": self_ans,
            "mark": mark,
            "correct": correct,
            "unclear": qnum in memo,
            "domain": domain,
        })
        i = j
    return {"exam_id": exam_id, "final_score": final_score, "memo": memo,
            "questions": questions}


def main():
    out = []
    for path, eid, score in EXAMS:
        data = parse_exam(path, eid, score)
        out.append(data)
    # summary
    summary = {}
    for exam in out:
        per_domain = {}
        for q in exam["questions"]:
            d = q["domain"]
            per_domain.setdefault(d, {"total": 0, "correct": 0, "wrong": [], "unclear": []})
            per_domain[d]["total"] += 1
            if q["correct"]:
                per_domain[d]["correct"] += 1
            else:
                per_domain[d]["wrong"].append(q["q"])
            if q["unclear"]:
                per_domain[d]["unclear"].append(q["q"])
        summary[f"exam{exam['exam_id']}"] = per_domain

    result = {"exams": out, "summary": summary}
    out_path = ROOT / "dist" / "mock_exam_data.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {out_path}")
    # brief report
    for exam in out:
        total = len(exam["questions"])
        correct = sum(1 for q in exam["questions"] if q["correct"])
        print(f"Exam {exam['exam_id']}: {correct}/{total} correct, final score {exam['final_score']}")
        per = summary[f"exam{exam['exam_id']}"]
        for d in sorted(per.keys()):
            v = per[d]
            pct = (v["correct"] / v["total"] * 100) if v["total"] else 0
            print(f"  {d}: {v['correct']}/{v['total']} ({pct:.0f}%) wrong={v['wrong']}")


if __name__ == "__main__":
    main()
