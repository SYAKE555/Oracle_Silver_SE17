#!/usr/bin/env python3
"""Parse mock exam text files into structured JSON for analysis."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXAM_SOURCES = [
    {"path": ROOT / "模擬問題一回目　記録　48点.txt", "exam_id": 1, "title": "第1回 模擬試験"},
    {"path": ROOT / "模擬問題二回目　記録　33点.txt", "exam_id": 2, "title": "第2回 模擬試験"},
    {"path": ROOT / "模擬試験三回目　記録　34点.txt", "exam_id": 3, "title": "第3回 模擬試験"},
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
    "D1": [
        "リレーショナル", "主キー", "外部キー", "一意キー", "ERD", "正規化",
        "DDL", "DML", "DCL", "TCL", "オブジェクト型", "NULL値を持たせ",
        "DUAL", "スキーマ", "データベース管理",
    ],
    "D2": [
        "LIKE", "ワイルドカード", "ORDER BY", "ROWNUM", "FETCH", "OFFSET",
        "置換変数", "VERIFY", "BETWEEN", "WHERE", " IN ", "比較演算子",
        "ASC", "DESC", "NULLS FIRST", "NULLS LAST",
    ],
    "D3": [
        "UPPER", "LOWER", "INITCAP", "SUBSTR", "INSTR", "LENGTH", "LPAD",
        "RPAD", "TRIM", "REPLACE", "CONCAT", "ROUND", "TRUNC", "MOD",
        "SYSDATE", "CURRENT_DATE", "MONTHS_BETWEEN", "ADD_MONTHS",
        "NEXT_DAY", "LAST_DAY", "EXTRACT", "TO_CHAR", "TO_DATE",
        "TO_NUMBER", "NVL", "NVL2", "NULLIF", "COALESCE", "CASE", "DECODE",
        "暗黙的", "単一行関数",
    ],
    "D4": [
        "GROUP BY", "HAVING", "SUM(", "AVG(", "MAX(", "MIN(", "COUNT(",
        "グループ関数", "集計", "ROLLUP", "CUBE",
    ],
    "D5": ["JOIN", "INNER", "OUTER", "CROSS", "NATURAL", "USING", " ON ", "結合", "自己結合", "デカルト"],
    "D6": ["サブクエリ", "副問合せ", "EXISTS", "NOT EXISTS", "UNION", "INTERSECT", "MINUS", "ANY", " ALL ", "相関"],
    "D7": [
        "INSERT", "UPDATE", "DELETE", "MERGE", "TRUNCATE", "COMMIT",
        "ROLLBACK", "SAVEPOINT", "トランザクション", "マルチテーブル",
        "行レベルロック",
    ],
    "D8": [
        "CREATE TABLE", "ALTER TABLE", "DROP TABLE", "VIEW", "SEQUENCE",
        "INDEX", "SYNONYM", "GRANT", "REVOKE", "ROLE", "権限", "ロール",
        "制約", "CHECK", "NOT NULL", "UNIQUE", "PRIMARY KEY",
        "FOREIGN KEY", "辞書", "ディクショナリ", "TIMESTAMP", "INTERVAL",
        "タイムゾーン", "WITH TIME ZONE",
    ],
}

ALL_DOMAINS = tuple(sorted(DOMAIN_KEYWORDS))
SCORE_HINT = re.compile(r"(\d+)点")
Q_HEADER = re.compile(r"^問題(\d+)\s*第\d+問目\s*/\s*全(\d+)問")
ANS_LINE = re.compile(r"^Ans\.(.*)$")
SELFANS_LINE = re.compile(r"^(?:SelfAns|SA)\.(.*)$")
MARK_LINE = re.compile(r"^[○×]\s*$")


def classify(text: str) -> str:
    """Context-aware classifier returning best-matching domain."""
    upper = text.upper()

    ddl_context = any(
        kw in upper
        for kw in [
            "CREATE TABLE", "ALTER TABLE", "DROP TABLE",
            "CREATE VIEW", "DROP VIEW", "CREATE OR REPLACE VIEW",
            "CREATE SEQUENCE", "ALTER SEQUENCE", "CREATE INDEX",
            "CREATE SYNONYM", "GRANT ", "REVOKE ", "ロール",
            "CREATE USER", "CREATE ROLE", "データ・ディクショナリ",
            "USER_TABLES", "USER_CONSTRAINTS", "USER_TAB_COLUMNS",
            "ALL_TABLES", "DBA_TABLES", "TIMESTAMP WITH", "INTERVAL ",
            "タイムゾーン", "WITH TIME ZONE", "シノニム", "シーケンス",
            "ビュー", "READ ONLY", "CHECK OPTION", "INVISIBLE", "PUBLIC SYNONYM",
        ]
    )
    if "制約" in text and ddl_context:
        return "D8"
    if ddl_context:
        return "D8"

    if any(
        kw in upper
        for kw in [
            "INSERT INTO", "INSERT ALL", "INSERT FIRST", "UPDATE ",
            "DELETE FROM", "MERGE INTO", "TRUNCATE TABLE", "COMMIT",
            "ROLLBACK", "SAVEPOINT", "トランザクション", "マルチテーブル",
        ]
    ):
        return "D7"

    if any(kw in upper for kw in ["UNION ALL", "UNION", "INTERSECT", "MINUS", "EXISTS", "サブクエリ", "副問合せ", "相関"]):
        return "D6"
    if re.search(r"=\s*(ANY|ALL|SOME)\b", upper) or re.search(r"<\s*ANY\b|>\s*ANY\b", upper):
        return "D6"

    if any(kw in upper for kw in ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "CROSS JOIN", "NATURAL JOIN", "OUTER JOIN", "USING (", "JOIN ", "自己結合", "デカルト"]):
        return "D5"

    if any(kw in upper for kw in ["GROUP BY", "HAVING", "ROLLUP", "CUBE"]):
        return "D4"
    if re.search(r"\b(SUM|AVG|COUNT|MAX|MIN)\s*\(", upper) and "GROUP" in upper:
        return "D4"

    if any(
        kw in upper
        for kw in [
            "UPPER(", "LOWER(", "INITCAP(", "SUBSTR(", "INSTR(", "LENGTH(",
            "LPAD(", "RPAD(", "TRIM(", "REPLACE(", "CONCAT(",
            "ROUND(", "TRUNC(", "MOD(", "CEIL(", "FLOOR(",
            "SYSDATE", "CURRENT_DATE", "MONTHS_BETWEEN(", "ADD_MONTHS(",
            "NEXT_DAY(", "LAST_DAY(", "EXTRACT(",
            "TO_CHAR(", "TO_DATE(", "TO_NUMBER(",
            "NVL(", "NVL2(", "NULLIF(", "COALESCE(",
            "CASE ", "DECODE(", "単一行関数", "暗黙的",
        ]
    ):
        return "D3"

    if any(
        kw in upper
        for kw in [
            "LIKE", "ワイルドカード", "ORDER BY", "ROWNUM", "FETCH FIRST",
            "OFFSET", "置換変数", "VERIFY", "BETWEEN", " IN (",
            "NULLS FIRST", "NULLS LAST", "IS NULL", "IS NOT NULL", "WHERE ",
        ]
    ):
        return "D2"

    return "D1"


def pct(correct: int, total: int) -> float:
    return (correct / total * 100.0) if total else 0.0


def parse_score(text: str, path: Path) -> int:
    first_non_empty = next((line.strip() for line in text.splitlines() if line.strip()), "")
    for candidate in (first_non_empty, path.stem):
        match = SCORE_HINT.search(candidate)
        if match:
            return int(match.group(1))
    raise ValueError(f"Could not determine final score from {path}")


def normalize_answer(answer: str | None) -> str | None:
    if answer is None:
        return None
    return re.sub(r"\s+", "", answer).upper()


def parse_exam(path: Path, exam_id: int, title: str) -> dict:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    final_score = parse_score(text, path)

    memo = []
    for line in lines[:40]:
        match = re.match(r"^・問(\d+)", line.strip())
        if match:
            memo.append(int(match.group(1)))

    questions = []
    declared_total = None
    i = 0
    while i < len(lines):
        header = Q_HEADER.match(lines[i].strip())
        if not header:
            i += 1
            continue
        qnum = int(header.group(1))
        declared_total = int(header.group(2))

        body = []
        j = i + 1
        while j < len(lines) and not Q_HEADER.match(lines[j].strip()):
            body.append(lines[j])
            j += 1

        ans = None
        self_ans = None
        mark = None
        q_text_lines = []
        for raw in body:
            stripped = raw.strip()
            if ans is None:
                ans_match = ANS_LINE.match(stripped)
                if ans_match:
                    ans = ans_match.group(1).strip()
                    continue
            if self_ans is None:
                self_match = SELFANS_LINE.match(stripped)
                if self_match:
                    self_ans = self_match.group(1).strip()
                    continue
            if MARK_LINE.match(stripped):
                mark = stripped
                continue
            q_text_lines.append(raw)

        if mark is None:
            if ans and self_ans:
                mark = "○" if normalize_answer(ans) == normalize_answer(self_ans) else "×"
            elif ans and self_ans is None:
                mark = "○"
            elif self_ans:
                mark = "×"
            else:
                mark = "?"

        q_text = "\n".join(q_text_lines).strip()
        domain = classify(f"{q_text} {ans or ''}")
        questions.append(
            {
                "exam": exam_id,
                "q": qnum,
                "text": q_text,
                "ans": ans,
                "self_ans": self_ans,
                "mark": mark,
                "correct": mark == "○",
                "unclear": qnum in memo,
                "domain": domain,
            }
        )
        i = j

    total_questions = declared_total or len(questions)
    correct_questions = sum(1 for question in questions if question["correct"])
    wrong_questions = total_questions - correct_questions
    return {
        "exam_id": exam_id,
        "title": title,
        "source_file": path.name,
        "final_score": final_score,
        "score_ratio": float(final_score),
        "total_questions": total_questions,
        "correct_questions": correct_questions,
        "wrong_questions": wrong_questions,
        "accuracy": pct(correct_questions, total_questions),
        "memo": memo,
        "questions": questions,
    }


def summarise_questions(questions: list[dict]) -> dict:
    per_domain = {
        domain: {"total": 0, "correct": 0, "wrong": [], "unclear": [], "accuracy": 0.0}
        for domain in ALL_DOMAINS
    }
    for question in questions:
        bucket = per_domain[question["domain"]]
        bucket["total"] += 1
        if question["correct"]:
            bucket["correct"] += 1
        else:
            bucket["wrong"].append(question["q"])
        if question["unclear"]:
            bucket["unclear"].append(question["q"])
    for values in per_domain.values():
        values["accuracy"] = pct(values["correct"], values["total"])
    return per_domain


def build_dataset() -> dict:
    exams = [parse_exam(item["path"], item["exam_id"], item["title"]) for item in EXAM_SOURCES]
    by_exam = {}
    combined = {
        domain: {"total": 0, "correct": 0, "wrong": [], "unclear": [], "accuracy": 0.0}
        for domain in ALL_DOMAINS
    }

    for exam in exams:
        per_domain = summarise_questions(exam["questions"])
        by_exam[f"exam{exam['exam_id']}"] = per_domain
        for domain in ALL_DOMAINS:
            combined[domain]["total"] += per_domain[domain]["total"]
            combined[domain]["correct"] += per_domain[domain]["correct"]
            combined[domain]["wrong"].extend(
                {"exam_id": exam["exam_id"], "q": qnum}
                for qnum in per_domain[domain]["wrong"]
            )
            combined[domain]["unclear"].extend(
                {"exam_id": exam["exam_id"], "q": qnum}
                for qnum in per_domain[domain]["unclear"]
            )

    for values in combined.values():
        values["accuracy"] = pct(values["correct"], values["total"])

    overall_total = sum(exam["total_questions"] for exam in exams)
    overall_correct = sum(exam["correct_questions"] for exam in exams)
    average_score = sum(exam["final_score"] for exam in exams) / len(exams)

    return {
        "exams": exams,
        "summary": {
            "by_exam": by_exam,
            "combined": combined,
            "overall": {
                "exam_count": len(exams),
                "question_count": overall_total,
                "correct_questions": overall_correct,
                "wrong_questions": overall_total - overall_correct,
                "accuracy": pct(overall_correct, overall_total),
                "average_score": average_score,
                "average_score_ratio": average_score,
            },
        },
    }


def write_dataset(dataset: dict) -> Path:
    out_path = ROOT / "dist" / "mock_exam_data.json"
    out_path.write_text(json.dumps(dataset, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path


def main() -> None:
    dataset = build_dataset()
    out_path = write_dataset(dataset)
    print(f"Wrote {out_path}")
    for exam in dataset["exams"]:
        print(
            f"Exam {exam['exam_id']}: "
            f"score {exam['final_score']} / accuracy {exam['accuracy']:.1f}% "
            f"({exam['correct_questions']}/{exam['total_questions']})"
        )
        for domain in ALL_DOMAINS:
            values = dataset["summary"]["by_exam"][f"exam{exam['exam_id']}"][domain]
            if values["total"] == 0:
                continue
            print(
                f"  {domain}: {values['correct']}/{values['total']} "
                f"({values['accuracy']:.0f}%) wrong={values['wrong']}"
            )


if __name__ == "__main__":
    main()
