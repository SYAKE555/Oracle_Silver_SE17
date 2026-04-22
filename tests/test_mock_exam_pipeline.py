#!/usr/bin/env python3
"""Regression tests for mock exam parsing and aggregation."""

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_module(module_name: str, relative_path: str):
    spec = importlib.util.spec_from_file_location(module_name, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


parse_mock_exams = load_module("parse_mock_exams", "scripts/parse_mock_exams.py")
split_ex_pages = load_module("split_ex_pages", "scripts/split_ex_pages.py")


class TestMockExamPipeline(unittest.TestCase):
    def test_build_dataset_includes_three_exams(self):
        dataset = parse_mock_exams.build_dataset()

        self.assertEqual(dataset["summary"]["overall"]["exam_count"], 3)
        self.assertEqual([exam["exam_id"] for exam in dataset["exams"]], [1, 2, 3])
        self.assertEqual([exam["final_score"] for exam in dataset["exams"]], [48, 33, 34])

    def test_sa_alias_is_parsed_as_self_answer(self):
        exam = parse_mock_exams.parse_exam(
            ROOT / "模擬試験三回目　記録　34点.txt",
            3,
            "第3回 模擬試験",
        )

        third_question = next(question for question in exam["questions"] if question["q"] == 3)
        self.assertEqual(third_question["self_ans"], "D")
        self.assertFalse(third_question["correct"])
        self.assertEqual(exam["correct_questions"], 27)

    def test_phase_priority_order_matches_weak_domains(self):
        ranked = split_ex_pages.priority_data()
        phases = split_ex_pages.assign_phases(ranked)

        self.assertEqual([item["ex_id"] for item in ranked[:3]], ["EX2", "EX3", "EX5"])
        self.assertEqual([len(phase["items"]) for phase in phases], [3, 3, 2])

    def test_domain_pages_cover_all_wrong_questions(self):
        ranked = split_ex_pages.priority_data()
        split_ex_pages.assign_phases(ranked)

        for item in ranked:
            html = split_ex_pages.build_domain_page(item, review_mode="wrong")
            self.assertEqual(html.count('class="question-card"'), item["wrong_count"])

    def test_domain_pages_cover_all_correct_questions(self):
        ranked = split_ex_pages.priority_data()
        split_ex_pages.assign_phases(ranked)
        dataset = json.loads((ROOT / "dist" / "mock_exam_data.json").read_text(encoding="utf-8"))

        combined = dataset["summary"]["combined"]
        for item in ranked:
            html = split_ex_pages.build_domain_page(item, review_mode="correct")
            self.assertEqual(html.count('class="question-card"'), combined[item["domain"]]["correct"])

    def test_detect_concept_for_known_quality_sensitive_questions(self):
        dataset = json.loads((ROOT / "dist" / "mock_exam_data.json").read_text(encoding="utf-8"))
        expected = {
            (2, 25): "self_join_vs_subquery",
            (2, 34): "set_operator_general",
            (2, 60): "set_operator_general",
            (2, 62): "subquery_usage",
            (3, 39): "single_row_function_basics",
            (3, 63): "set_operator_general",
            (3, 69): "multiple_row_subquery",
            (1, 42): "update_syntax",
        }

        actual = {}
        for exam in dataset["exams"]:
            for question in exam["questions"]:
                key = (exam["exam_id"], question["q"])
                if key in expected:
                    actual[key] = split_ex_pages.detect_concept(question["domain"], question["text"])

        self.assertEqual(actual, expected)

    def test_hub_and_phase_pages_link_expected_ex_pages(self):
        ranked = split_ex_pages.priority_data()
        phases = split_ex_pages.assign_phases(ranked)

        hub_html = split_ex_pages.build_hub_page(phases)
        self.assertIn("Phase 1 最優先再構築", hub_html)
        self.assertIn("phase1_reinforce.html", hub_html)
        self.assertIn("EX2_reinforce.html", hub_html)
        self.assertIn("EX8_reinforce.html", hub_html)

        phase1_html = split_ex_pages.build_phase_page(phases[0])
        self.assertIn("EX2_reinforce.html", phase1_html)
        self.assertIn("EX3_reinforce.html", phase1_html)
        self.assertIn("EX5_reinforce.html", phase1_html)
        correct_hub_html = split_ex_pages.build_correct_hub_page(ranked)
        self.assertIn("EX2_correct.html", correct_hub_html)
        self.assertIn("EX8_correct.html", correct_hub_html)

        dashboard_html = split_ex_pages.build_center_page(ranked)
        self.assertIn("mock_exam_report.html", dashboard_html)
        self.assertIn("mock_exam_reinforce.html", dashboard_html)
        self.assertIn("mock_exam_correct.html", dashboard_html)
    def test_domain_page_uses_recorded_full_text_as_canonical_problem(self):
        ranked = split_ex_pages.priority_data()
        split_ex_pages.assign_phases(ranked)
        ex2 = next(item for item in ranked if item["ex_id"] == "EX2")

        html = split_ex_pages.build_domain_page(ex2, review_mode="wrong")

        self.assertIn("問題文", html)
        self.assertNotIn('<div class="block-title">選択肢</div>', html)
        self.assertNotIn("記録原文（省略なし）", html)
        self.assertNotIn("（抽出）", html)
        self.assertIn('SELECT dummy &quot;DUMMY1&quot; FROM DUAL', html)
        self.assertIn("INTERSECT", html)


if __name__ == "__main__":
    unittest.main()
