"""
Unit tests for comparison assertions using unittest.
"""

import unittest

class TestAssertGreater(unittest.TestCase):
    """Test cases for assertGreater method."""

    def test_positive(self):
        """Test that the first value is greater than the second."""
        self.assertGreater(6, 5, "First value should be greater than second")

    def test_negative(self):
        """Test that an AssertionError is raised when the first value is not greater."""
        with self.assertRaises(AssertionError):
            self.assertGreater(5, 6, "First value should not be greater than second")

if __name__ == '__main__':
    unittest.main()
