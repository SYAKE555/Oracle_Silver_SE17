#!/usr/bin/env python3
"""Extract wrong-answered questions grouped by domain for Codex briefing."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "dist" / "mock_exam_data.json").read_text(encoding="utf-8"))

by_domain: dict = {}
for exam in data["exams"]:
    for q in exam["questions"]:
        if not q["correct"]:
            by_domain.setdefault(q["domain"], []).append({
                "exam": exam["exam_id"],
                "q": q["q"],
                "text": q["text"],
                "ans": q["ans"],
                "self_ans": q["self_ans"],
            })

out = ROOT / "dist" / "wrong_by_domain.json"
out.write_text(json.dumps(by_domain, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {out}")
for d in sorted(by_domain.keys()):
    print(f"{d}: {len(by_domain[d])} 問")
