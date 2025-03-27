"""
Unit tests for assertIsNone method in unittest.
"""

import unittest

class TestAssertIsNone(unittest.TestCase):
    """Test cases for assertIsNone assertions."""

    def test_positive(self):
        """Test that assertIsNone passes when the value is None."""
        self.assertIsNone(None, "Value should be None")

    def test_negative(self):
        """Test that assertIsNone raises an error when the value is not None."""
        with self.assertRaises(AssertionError):
            self.assertIsNone("not None", "Value should not be None")

if __name__ == '__main__':
    unittest.main()
