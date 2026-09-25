"""In-process API tests."""

import unittest

from fastapi.testclient import TestClient

from app.main import app


class GenerateEndpointTests(unittest.TestCase):
    """Verify the public random-number generation endpoint."""

    def test_post_generate_returns_number_in_half_open_unit_interval(self) -> None:
        response = TestClient(app).post("/generate")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn("number", payload)
        self.assertIsInstance(payload["number"], (int, float))
        self.assertGreaterEqual(payload["number"], 0.0)
        self.assertLess(payload["number"], 1.0)


if __name__ == "__main__":
    unittest.main()
