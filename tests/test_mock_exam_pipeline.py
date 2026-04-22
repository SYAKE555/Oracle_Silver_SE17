#!/usr/bin/env python3
"""Regression tests for mock exam parsing and aggregation."""

import importlib.util
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


if __name__ == "__main__":
    unittest.main()
