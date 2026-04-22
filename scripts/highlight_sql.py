#!/usr/bin/env python3
"""Colorize SQL reserved words, functions, literals, and comments inside
<pre> blocks across every generated textbook / mock-exam HTML page.

Idempotent: <pre> blocks that already contain an sql-kw span are skipped,
and CSS rules are inserted only once per file.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_DIRS = ["textbooks", "dist"]

KEYWORDS_MULTI = [
    "WITH GRANT OPTION",
    "NOT NULL",
    "GROUP BY", "ORDER BY",
    "PRIMARY KEY", "FOREIGN KEY",
    "UNION ALL",
    "START WITH", "INCREMENT BY",
    "INNER JOIN", "LEFT OUTER JOIN", "RIGHT OUTER JOIN", "FULL OUTER JOIN",
    "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "CROSS JOIN", "NATURAL JOIN",
    "OUTER JOIN",
    "WHEN MATCHED", "WHEN NOT MATCHED",
    "FETCH FIRST", "ROWS ONLY", "ROWS ONLY",
    "IS NULL", "IS NOT NULL",
    "NOT IN", "NOT EXISTS",
    "WITH READ ONLY", "WITH CHECK OPTION",
    "ON DELETE CASCADE", "ON DELETE SET NULL",
    "DROP COLUMN", "ADD COLUMN",
    "MERGE INTO",
    "INSERT INTO", "INSERT ALL", "INSERT FIRST",
    "DELETE FROM",
    "CREATE TABLE", "CREATE VIEW", "CREATE INDEX", "CREATE SEQUENCE",
    "CREATE SYNONYM", "CREATE OR REPLACE",
    "ALTER TABLE", "ALTER SESSION",
    "DROP TABLE", "DROP VIEW", "DROP INDEX", "DROP SEQUENCE", "DROP SYNONYM",
    "TRUNCATE TABLE",
    "ROLLBACK TO",
]

KEYWORDS_SINGLE = [
    "SELECT", "FROM", "WHERE", "HAVING",
    "JOIN", "ON", "USING",
    "UNION", "INTERSECT", "MINUS",
    "INSERT", "INTO", "VALUES", "UPDATE", "SET", "DELETE", "MERGE",
    "WHEN", "MATCHED", "THEN", "ELSE", "END",
    "CREATE", "TABLE", "ALTER", "ADD", "MODIFY", "DROP", "COLUMN",
    "VIEW", "INDEX", "SEQUENCE", "SYNONYM", "PUBLIC",
    "GRANT", "REVOKE", "TO", "FOR", "OF",
    "AS", "WITH", "DEFAULT", "NOT", "NULL", "IS",
    "REFERENCES", "UNIQUE", "CHECK", "CONSTRAINT",
    "COMMIT", "ROLLBACK", "SAVEPOINT",
    "EXISTS", "IN", "ANY", "ALL", "SOME", "AND", "OR",
    "BETWEEN", "LIKE", "ESCAPE",
    "DISTINCT", "CASE",
    "FETCH", "FIRST", "NEXT", "ROWS", "ONLY", "OFFSET",
    "ASC", "DESC", "TRUNCATE",
    "CURRVAL", "NEXTVAL", "DUAL",
    "BY", "DESCRIBE",
    "INNER", "LEFT", "RIGHT", "FULL", "OUTER", "CROSS", "NATURAL",
    "CASCADE", "RESTRICT",
]

FUNCTIONS = [
    "CURRENT_TIMESTAMP", "CURRENT_DATE", "SYSTIMESTAMP", "SYSDATE", "LOCALTIMESTAMP",
    "MONTHS_BETWEEN", "ADD_MONTHS", "LAST_DAY", "NEXT_DAY", "EXTRACT", "NEW_TIME",
    "TO_CHAR", "TO_NUMBER", "TO_DATE", "TO_TIMESTAMP",
    "NVL2", "NVL", "COALESCE", "NULLIF", "DECODE", "CAST",
    "UPPER", "LOWER", "INITCAP", "SUBSTR", "INSTR", "LENGTH", "LENGTHB",
    "TRIM", "LTRIM", "RTRIM", "REPLACE", "LPAD", "RPAD", "CHR", "ASCII", "CONCAT",
    "ROUND", "TRUNC", "CEIL", "FLOOR", "ABS", "MOD", "POWER", "SIGN", "SQRT", "REMAINDER",
    "COUNT", "SUM", "AVG", "MIN", "MAX", "STDDEV", "VARIANCE", "LISTAGG",
    "GREATEST", "LEAST",
]

ALL_MULTI = sorted(KEYWORDS_MULTI, key=len, reverse=True)
ALL_SINGLE = sorted(set(KEYWORDS_SINGLE), key=len, reverse=True)
ALL_FN = sorted(set(FUNCTIONS), key=len, reverse=True)

# Build a single master pattern; order of alternatives matters (first win).
PATTERN = re.compile(
    r"(?P<cmt>--[^\n]*)"
    r"|(?P<str>'(?:[^']|'')*')"
    r"|(?P<kw_m>\b(?:" + "|".join(re.escape(w) for w in ALL_MULTI) + r")\b)"
    r"|(?P<fn>\b(?:" + "|".join(re.escape(w) for w in ALL_FN) + r")(?=\s*\())"
    r"|(?P<kw_s>\b(?:" + "|".join(re.escape(w) for w in ALL_SINGLE) + r")\b)"
    r"|(?P<num>\b\d+(?:\.\d+)?\b)"
)

CSS_RULES = (
    "\n  pre .sql-kw { color: #fbbf24; font-weight: 700; }"
    "\n  pre .sql-fn { color: #60a5fa; font-weight: 600; }"
    "\n  pre .sql-str { color: #86efac; }"
    "\n  pre .sql-num { color: #fca5a5; }"
    "\n  pre .sql-cmt { color: #94a3b8; font-style: italic; }"
    "\n  code .sql-kw { color: #b45309; font-weight: 700; }"
    "\n  code .sql-fn { color: #1d4ed8; font-weight: 600; }"
    "\n  code .sql-str { color: #047857; }"
    "\n  code .sql-num { color: #b91c1c; }"
    "\n  code .sql-cmt { color: #64748b; font-style: italic; }"
)

PRE_BLOCK = re.compile(r"(<pre\b[^>]*>)(.*?)(</pre>)", re.DOTALL)
CODE_BLOCK = re.compile(r"(<code\b[^>]*>)(.*?)(</code>)", re.DOTALL)
STYLE_CLOSE = re.compile(r"</style>")
TAG_SPLIT = re.compile(r"(<[^>]+>)")


def _wrap(m: re.Match) -> str:
    for name, cls in (("cmt", "sql-cmt"), ("str", "sql-str"),
                      ("kw_m", "sql-kw"), ("fn", "sql-fn"),
                      ("kw_s", "sql-kw"), ("num", "sql-num")):
        if m.group(name) is not None:
            return f'<span class="{cls}">{m.group(name)}</span>'
    return m.group(0)


def colorize_text(escaped: str) -> str:
    # Operate only on text segments; never cross an existing tag boundary.
    parts = TAG_SPLIT.split(escaped)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:  # tag
            out.append(part)
        else:
            out.append(PATTERN.sub(_wrap, part))
    return "".join(out)


def process_block(match: re.Match) -> str:
    open_tag, body, close_tag = match.group(1), match.group(2), match.group(3)
    if "sql-kw" in body or "sql-fn" in body:
        return match.group(0)
    return open_tag + colorize_text(body) + close_tag


def inject_css(html: str) -> str:
    if ".sql-kw" in html:
        return html
    return STYLE_CLOSE.sub(CSS_RULES + "\n</style>", html, count=1)


def process_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    new = PRE_BLOCK.sub(process_block, html)
    new = CODE_BLOCK.sub(process_block, new)
    new = inject_css(new)
    if new != html:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    touched = 0
    for sub in TARGET_DIRS:
        for path in sorted((ROOT / sub).glob("*.html")):
            if process_file(path):
                touched += 1
                print(f"highlighted {path}")
    print(f"done: {touched} files updated")


if __name__ == "__main__":
    main()
