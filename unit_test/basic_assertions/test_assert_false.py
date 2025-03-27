"""Unit tests for assertFalse assertions."""

import unittest

class TestAssertFalse(unittest.TestCase):
    """Test cases for assertFalse assertions."""

    def test_positive(self):
        """Test that a false value passes assertFalse."""
        self.assertFalse(1 > 2, "Value should be false")

    def test_negative(self):
        """Test that a true value raises an AssertionError with assertFalse."""
        with self.assertRaises(AssertionError):
            self.assertFalse(2 > 1, "Value should not be false")

if __name__ == '__main__':
    unittest.main()
