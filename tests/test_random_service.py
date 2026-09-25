"""Tests for the pure random-number service."""

import unittest

from app.random_service import generate_random_number


class GenerateRandomNumberTests(unittest.TestCase):
    """Verify the random-number service contract."""

    def test_generates_float_in_half_open_unit_interval(self) -> None:
        result = generate_random_number()

        self.assertIsInstance(result, float)
        self.assertGreaterEqual(result, 0.0)
        self.assertLess(result, 1.0)


if __name__ == "__main__":
    unittest.main()
