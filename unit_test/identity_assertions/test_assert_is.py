"""
This module contains unit tests for identity assertions using unittest.
"""

import unittest

class TestAssertIs(unittest.TestCase):
    """Test cases for identity assertions."""

    def test_positive(self):
        """Test that two references to the same object are identical."""
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b, "Objects should be identical")

    def test_negative(self):
        """Test that two different objects are not identical."""
        a = [1, 2, 3]
        b = [1, 2, 3]
        with self.assertRaises(AssertionError):
            self.assertIs(a, b, "Objects should not be identical")

if __name__ == '__main__':
    unittest.main()
