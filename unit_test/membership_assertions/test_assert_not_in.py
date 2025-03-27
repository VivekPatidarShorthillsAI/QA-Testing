"""
Unit tests for assertNotIn assertions.
"""

import unittest

class TestAssertNotIn(unittest.TestCase):
    """Test cases for assertNotIn assertions."""

    def test_positive(self):
        """Test that a value is not in the container."""
        self.assertNotIn("d", ["a", "b", "c"], "Value should not be in container")

    def test_negative(self):
        """Test that an AssertionError is raised when the value is in the container."""
        with self.assertRaises(AssertionError):
            self.assertNotIn("a", ["a", "b", "c"], "Value should be in container")

if __name__ == '__main__':
    unittest.main()
    