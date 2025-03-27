"""Unit tests for floating-point assertions using assertAlmostEqual."""

import unittest

class TestAssertAlmostEqual(unittest.TestCase):
    """Test cases for assertAlmostEqual with places and delta."""

    def test_positive_with_places(self):
        """Test assertAlmostEqual with positive case using places."""
        self.assertAlmostEqual(
            1.00001, 1.0, places=3, msg="Values should be almost equal"
        )

    def test_positive_with_delta(self):
        """Test assertAlmostEqual with positive case using delta."""
        self.assertAlmostEqual(
            1.00001, 1.0, delta=0.0001, msg="Values should be almost equal"
        )

    def test_negative_with_places(self):
        """Test assertAlmostEqual with negative case using places."""
        with self.assertRaises(AssertionError):
            self.assertAlmostEqual(
                1.0005, 1.0, places=4, msg="Values should not be almost equal"
            )

    def test_negative_with_delta(self):
        """Test assertAlmostEqual with negative case using delta."""
        with self.assertRaises(AssertionError):
            self.assertAlmostEqual(
                1.0005, 1.0, delta=0.0001, msg="Values should not be almost equal"
            )

if __name__ == '__main__':
    unittest.main()
