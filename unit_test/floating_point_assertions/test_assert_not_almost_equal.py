"""
Unit tests for assertNotAlmostEqual method in unittest.
"""

import unittest

class TestAssertNotAlmostEqual(unittest.TestCase):
    """Test cases for assertNotAlmostEqual assertions."""

    def test_positive_with_places(self):
        """Test assertNotAlmostEqual with places argument for positive case."""
        self.assertNotAlmostEqual(1.0005, 1.0, places=4)

    def test_positive_with_delta(self):
        """Test assertNotAlmostEqual with delta argument for positive case."""
        self.assertNotAlmostEqual(1.0005, 1.0, delta=0.0001)

    def test_negative_with_places(self):
        """Test assertNotAlmostEqual with places argument for negative case."""
        with self.assertRaises(AssertionError):
            self.assertNotAlmostEqual(1.00001, 1.0, places=3)

    def test_negative_with_delta(self):
        """Test assertNotAlmostEqual with delta argument for negative case."""
        with self.assertRaises(AssertionError):
            self.assertNotAlmostEqual(1.00001, 1.0, delta=0.0001)

if __name__ == '__main__':
    unittest.main()
    