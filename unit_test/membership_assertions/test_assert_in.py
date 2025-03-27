"""
This module contains unit tests for membership assertions using unittest.
"""

import unittest

class TestAssertIn(unittest.TestCase):
    """Test cases for assertIn assertions."""

    def test_positive(self):
        """Test that a value is in the container."""
        self.assertIn("a", ["a", "b", "c"], "Value should be in container")

    def test_negative(self):
        """Test that a value is not in the container."""
        with self.assertRaises(AssertionError):
            self.assertIn("d", ["a", "b", "c"], "Value should not be in container")

if __name__ == '__main__':
    unittest.main()
