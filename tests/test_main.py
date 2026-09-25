"""Regression coverage for the random-letter API endpoint."""

import unittest

from fastapi.testclient import TestClient

from app.main import app


class GenerateLetterEndpointTests(unittest.TestCase):
    """Verify the public random-letter generation endpoint."""

    def test_get_generate_letter_returns_one_uppercase_english_letter(self) -> None:
        response = TestClient(app).get("/generate-letter")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(set(payload), {"letter"})
        self.assertIsInstance(payload["letter"], str)
        self.assertEqual(len(payload["letter"]), 1)
        self.assertIn(payload["letter"], "ABCDEFGHIJKLMNOPQRSTUVWXYZ")


if __name__ == "__main__":
    unittest.main()
