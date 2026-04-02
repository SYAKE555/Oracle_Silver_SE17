#!/usr/bin/env python3
"""Simple HTML quality guard for textbook deliverables.

Checks:
- single html file readability basics
- no external JS/CSS/CDN references
- JS-free constraint
- responsive markers
- basic chapter-1 scope guard
"""

import re
import sys
from pathlib import Path


def fail(msg: str) -> None:
    print(f"[ERROR] {msg}")


def info(msg: str) -> None:
    print(f"[INFO] {msg}")


def main() -> int:
    if len(sys.argv) < 2:
        fail("Usage: python3 html_quality_guard.py <html_path>")
        return 1

    target = Path(sys.argv[1])
    if not target.exists():
        fail(f"File not found: {target}")
        return 1

    html = target.read_text(encoding="utf-8")
    errors = []

    # Basic structure
    if "<!DOCTYPE html>" not in html:
        errors.append("Missing <!DOCTYPE html>")
    if "<meta name=\"viewport\"" not in html:
        errors.append("Missing viewport meta")

    # JS/CSS external constraints
    if re.search(r"<script\b", html, re.IGNORECASE):
        errors.append("JS tag detected (<script>)")
    if re.search(r"<link[^>]+href=\"https?://", html, re.IGNORECASE):
        errors.append("External stylesheet link detected")
    if re.search(r"<script[^>]+src=\"https?://", html, re.IGNORECASE):
        errors.append("External JS detected")
    if re.search(r"https?://[^\"']*(cdn|cdnjs|jsdelivr|unpkg)", html, re.IGNORECASE):
        errors.append("CDN reference detected")

    # Responsive hint
    if "@media(" not in html.replace(" ", "") and "@media (" not in html:
        errors.append("No media query found for responsive support")

    # Scope guard for chapter-only deliverable
    if "第2章" in html or "第3章" in html or "第4章" in html:
        errors.append("Out-of-scope chapter mention detected (Chapter 2+)" )

    # Navigation checks
    if html.count('href="#') < 8:
        errors.append("Insufficient in-page anchor links (TOC may be weak)")

    if errors:
        fail(f"Quality check failed for: {target}")
        for e in errors:
            fail(f"- {e}")
        return 1

    info(f"Quality check passed: {target}")
    info("Checks: structure / no-js / no-external / responsive / scope / anchors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
