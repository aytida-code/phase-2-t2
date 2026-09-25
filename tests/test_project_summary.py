"""Regression coverage for the project summary documentation."""

from pathlib import Path
import unittest


class ProjectSummaryTests(unittest.TestCase):
    """Ensure the project summary remains present and accurate."""

    def test_summary_exists_and_describes_key_project_facts(self) -> None:
        summary_path = Path(__file__).resolve().parents[1] / "PROJECT_SUMMARY.md"

        self.assertTrue(summary_path.is_file())
        summary = summary_path.read_text(encoding="utf-8")
        for expected_fact in (
            "minimal FastAPI random-number API",
            "POST /generate",
            "generate_random_number()",
            "[0.0, 1.0)",
            "GeneratedNumber",
            "tests/test_api.py",
            "tests/test_random_service.py",
            "python -m unittest discover -s tests",
            "no database, authentication, messaging, pagination, frontend, or infrastructure",
        ):
            with self.subTest(expected_fact=expected_fact):
                self.assertIn(expected_fact, summary)


if __name__ == "__main__":
    unittest.main()
