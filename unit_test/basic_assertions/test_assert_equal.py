"""
This module contains unit tests for basic assertions using unittest.
"""

import unittest

class TestAssertEqual(unittest.TestCase):
    """Test cases for assertEqual method."""

    def test_positive(self):
        """Test that equal values pass the assertion."""
        self.assertEqual(5, 5, "Values should be equal")

    def test_negative(self):
        """Test that unequal values raise an AssertionError."""
        with self.assertRaises(AssertionError):
            self.assertEqual(5, 6, "Values should not be equal")

if __name__ == '__main__':
    unittest.main()
