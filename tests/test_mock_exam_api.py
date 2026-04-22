#!/usr/bin/env python3
"""API regression tests for mock exam dashboard endpoints."""

import importlib.util
import os
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_app_module():
    os.environ.setdefault("FLASK_SECRET_KEY", "test-secret-key")
    spec = importlib.util.spec_from_file_location("basetract_app", ROOT / "app.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


app_module = load_app_module()


class TestMockExamApi(unittest.TestCase):
    def test_dashboard_payload_contains_integrated_links(self):
        payload = app_module.build_mock_exam_dashboard_payload()

        self.assertIsNotNone(payload)
        self.assertEqual(payload["summary"]["exam_count"], 3)
        self.assertIn("/study/mock_exam_dashboard.html", payload["links"]["dashboard"])
        self.assertIn("/study/mock_exam_reinforce.html", payload["links"]["wrong_hub"])
        self.assertIn("/study/mock_exam_correct.html", payload["links"]["correct_hub"])
        self.assertTrue(payload["weakest_domains"])
        self.assertTrue(payload["strongest_domains"])

    def test_dashboard_endpoint_returns_json(self):
        client = app_module.app.test_client()
        response = client.get("/api/mock-exam/dashboard")

        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertEqual(body["summary"]["exam_count"], 3)
        self.assertIn("links", body)
        self.assertIn("weakest_domains", body)


if __name__ == "__main__":
    unittest.main()
