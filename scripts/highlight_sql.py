#!/usr/bin/env python3
"""Colorize SQL tokens inside <pre>/<code> AND inline prose text across every
generated textbook / mock-exam HTML page.  Also inserts <br> after Japanese
sentence-ending 。 to break long runs of text.

Idempotency: a versioned marker comment is embedded; re-running replaces the
CSS block but does not double-wrap already-colored tokens (existing <span>
elements are skipped during the inline walk).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TARGET_DIRS = ["textbooks", "dist"]

# ── keyword lists ─────────────────────────────────────────────────────────────
# Multi-word phrases must be matched before single words.
KEYWORDS_MULTI = [
    "WITH GRANT OPTION", "WITH READ ONLY", "WITH CHECK OPTION",
    "NOT NULL", "IS NOT NULL", "IS NULL", "NOT IN", "NOT EXISTS",
    "GROUP BY", "ORDER BY",
    "PRIMARY KEY", "FOREIGN KEY",
    "UNION ALL",
    "START WITH", "INCREMENT BY",
    "INNER JOIN", "LEFT OUTER JOIN", "RIGHT OUTER JOIN", "FULL OUTER JOIN",
    "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "CROSS JOIN", "NATURAL JOIN",
    "OUTER JOIN",
    "WHEN MATCHED", "WHEN NOT MATCHED",
    "FETCH FIRST", "ROWS ONLY",
    "ON DELETE CASCADE", "ON DELETE SET NULL",
    "DROP COLUMN", "DROP TABLE", "DROP VIEW", "DROP INDEX",
    "DROP SEQUENCE", "DROP SYNONYM",
    "CREATE TABLE", "CREATE VIEW", "CREATE INDEX", "CREATE SEQUENCE",
    "CREATE SYNONYM", "CREATE OR REPLACE",
    "ALTER TABLE", "ALTER SESSION",
    "TRUNCATE TABLE",
    "MERGE INTO", "INSERT INTO", "INSERT ALL", "INSERT FIRST",
    "DELETE FROM", "ROLLBACK TO",
    "NULLS FIRST", "NULLS LAST",
]

KEYWORDS_SINGLE = [
    "SELECT", "FROM", "WHERE", "HAVING",
    "JOIN", "ON", "USING",
    "UNION", "INTERSECT", "MINUS",
    "INSERT", "INTO", "VALUES", "UPDATE", "SET", "DELETE", "MERGE",
    "WHEN", "MATCHED", "THEN", "ELSE", "END",
    "CREATE", "TABLE", "ALTER", "ADD", "MODIFY", "DROP", "COLUMN",
    "VIEW", "INDEX", "SEQUENCE", "SYNONYM", "PUBLIC",
    "GRANT", "REVOKE", "TO",
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
    "UPPER", "LOWER", "INITCAP",
    "SUBSTR", "INSTR", "LENGTH", "LENGTHB",
    "TRIM", "LTRIM", "RTRIM", "REPLACE", "LPAD", "RPAD", "CHR", "ASCII", "CONCAT",
    "ROUND", "TRUNC", "CEIL", "FLOOR", "ABS", "MOD", "POWER", "SIGN", "SQRT",
    "COUNT", "SUM", "AVG", "MIN", "MAX", "STDDEV", "VARIANCE", "LISTAGG",
    "GREATEST", "LEAST",
]

# Sort longest first so multi-char alternatives win
ALL_MULTI  = sorted(KEYWORDS_MULTI,  key=len, reverse=True)
ALL_SINGLE = sorted(set(KEYWORDS_SINGLE), key=len, reverse=True)
ALL_FN     = sorted(set(FUNCTIONS),  key=len, reverse=True)

def _build_pattern(require_paren_for_fn: bool) -> re.Pattern:
    fn_lookahead = r"(?=\s*\()" if require_paren_for_fn else ""
    return re.compile(
        r"(?P<cmt>--[^\n]*)"
        r"|(?P<str>'(?:[^']|'')*')"
        r"|(?P<kw_m>\b(?:" + "|".join(re.escape(w) for w in ALL_MULTI)  + r")\b)"
        r"|(?P<fn>\b(?:"   + "|".join(re.escape(w) for w in ALL_FN)     + r")\b" + fn_lookahead + ")"
        r"|(?P<kw_s>\b(?:" + "|".join(re.escape(w) for w in ALL_SINGLE) + r")\b)"
        r"|(?P<num>\b\d+(?:\.\d+)?\b)"
    )

# In <pre>/<code>: highlight everything including comments, strings, bare numbers
PRE_PATTERN    = _build_pattern(require_paren_for_fn=True)
# In inline prose: functions only when followed by ( ; skip bare numbers to avoid
# false-positives on list indices / option numbers
INLINE_PATTERN = _build_pattern(require_paren_for_fn=True)

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS_MARKER = "/* sql-highlight-v3 */"

CSS_RULES = f"""
  {CSS_MARKER}
  /* default (light bg): warm tone */
  .sql-kw  {{ color: #92400e; font-weight: 700; }}
  .sql-fn  {{ color: #1e40af; font-weight: 600; }}
  .sql-str {{ color: #065f46; }}
  .sql-num {{ color: #991b1b; }}
  .sql-cmt {{ color: #64748b; font-style: italic; }}
  /* dark bg override (pre / code) */
  pre .sql-kw  {{ color: #fbbf24; }}
  pre .sql-fn  {{ color: #60a5fa; }}
  pre .sql-str {{ color: #86efac; }}
  pre .sql-num {{ color: #fca5a5; }}
  pre .sql-cmt {{ color: #94a3b8; }}
  code .sql-kw  {{ color: #fbbf24; }}
  code .sql-fn  {{ color: #60a5fa; }}
  code .sql-str {{ color: #86efac; }}
  code .sql-num {{ color: #fca5a5; }}
  code .sql-cmt {{ color: #94a3b8; }}
  /* clause-order div uses its own kw/fn/desc/note classes — no override needed */"""

# ── helpers ───────────────────────────────────────────────────────────────────
TAG_SPLIT   = re.compile(r"(<[^>]+>)")
PRE_BLOCK   = re.compile(r"(<pre\b[^>]*>)(.*?)(</pre>)",   re.DOTALL)
CODE_BLOCK  = re.compile(r"(<code\b[^>]*>)(.*?)(</code>)", re.DOTALL)
STYLE_BLOCK = re.compile(r"/\* sql-highlight[^*]*\*/.*?(?=\n\s*\n|\n</style>)", re.DOTALL)
STYLE_CLOSE = re.compile(r"</style>")


def _wrap(m: re.Match) -> str:
    for name, cls in (
        ("cmt",  "sql-cmt"),
        ("str",  "sql-str"),
        ("kw_m", "sql-kw"),
        ("fn",   "sql-fn"),
        ("kw_s", "sql-kw"),
        ("num",  "sql-num"),
    ):
        if m.group(name) is not None:
            return f'<span class="{cls}">{m.group(name)}</span>'
    return m.group(0)


def colorize_pre(content: str) -> str:
    """Highlight inside a <pre> or <code> block (tag-aware, idempotent)."""
    parts = TAG_SPLIT.split(content)
    out: list[str] = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part)
        else:
            out.append(PRE_PATTERN.sub(_wrap, part))
    return "".join(out)


def colorize_inline(text: str) -> str:
    """Highlight SQL tokens in a plain text node, then add 。<br> line breaks."""
    colored = INLINE_PATTERN.sub(_wrap, text)
    # Insert <br> after 。 when followed by more visible content (not end of node)
    broken = re.sub(r"。(?=\S)", "。<br>", colored)
    return broken


def process_pre_block(m: re.Match) -> str:
    open_tag, body, close_tag = m.group(1), m.group(2), m.group(3)
    if "sql-kw" in body or "sql-fn" in body:
        return m.group(0)
    return open_tag + colorize_pre(body) + close_tag


# Opening tags that create "skip" zones (content should not be re-colored)
VERBATIM_OPEN  = re.compile(r"^<(pre|code|script|style)\b", re.I)
VERBATIM_CLOSE = re.compile(r"^</(pre|code|script|style)>", re.I)
CLAUSE_OPEN    = re.compile(r'^<div\b[^>]*\bclass="clause-order"', re.I)
DIV_CLOSE      = re.compile(r"^</div>", re.I)
SPAN_OPEN      = re.compile(r"^<span\b", re.I)
SPAN_CLOSE     = re.compile(r"^</span>", re.I)


def process_inline_pass(html: str) -> str:
    """Walk every text node outside verbatim/span zones; apply inline coloring."""
    parts = TAG_SPLIT.split(html)
    out: list[str] = []

    verbatim_depth = 0   # inside pre/code/script/style
    span_depth     = 0   # inside any <span> (badges, sql-*, clause kw/fn spans)
    clause_depth   = 0   # inside .clause-order div (custom coloring, leave alone)

    for i, part in enumerate(parts):
        if i % 2 == 1:  # tag
            if VERBATIM_OPEN.match(part):
                verbatim_depth += 1
            elif VERBATIM_CLOSE.match(part):
                verbatim_depth = max(0, verbatim_depth - 1)
            elif CLAUSE_OPEN.match(part):
                clause_depth += 1
            elif DIV_CLOSE.match(part) and clause_depth > 0:
                clause_depth -= 1
            elif SPAN_OPEN.match(part):
                span_depth += 1
            elif SPAN_CLOSE.match(part):
                span_depth = max(0, span_depth - 1)
            out.append(part)
        else:  # text node
            skip = verbatim_depth > 0 or span_depth > 0 or clause_depth > 0
            if not skip and part.strip():
                out.append(colorize_inline(part))
            else:
                out.append(part)

    return "".join(out)


def inject_css(html: str) -> str:
    if CSS_MARKER in html:
        return html  # already current version
    # Strip previous sql-highlight CSS block if any version exists
    html = STYLE_BLOCK.sub("", html)
    # Strip any old-format rules left over from first version
    html = re.sub(
        r"\n  pre \.sql-kw \{.*?code \.sql-cmt \{[^}]*\}",
        "", html, flags=re.DOTALL
    )
    return STYLE_CLOSE.sub(CSS_RULES + "\n</style>", html, count=1)


def process_file(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    new = PRE_BLOCK.sub(process_pre_block, html)
    new = CODE_BLOCK.sub(process_pre_block, new)
    new = process_inline_pass(new)
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
