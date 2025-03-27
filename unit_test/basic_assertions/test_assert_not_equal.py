"""
This module contains unit tests for demonstrating the use of assertNotEqual in unittest.
"""

import unittest

class TestAssertNotEqual(unittest.TestCase):
    """Test cases for assertNotEqual assertions."""

    def test_positive(self):
        """Test that assertNotEqual passes when values are not equal."""
        self.assertNotEqual(5, 6, "Values should not be equal")

    def test_negative(self):
        """Test that assertNotEqual raises an AssertionError when values are equal."""
        with self.assertRaises(AssertionError):
            self.assertNotEqual(5, 5, "Values should be equal")

if __name__ == '__main__':
    unittest.main()
