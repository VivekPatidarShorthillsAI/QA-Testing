"""Module for testing assertTrue functionality."""

import unittest

class TestAssertTrue(unittest.TestCase):
    """Test cases for assertTrue assertions."""

    def test_positive(self):
        """Test that True is evaluated as true."""
        self.assertIs(True, True, "Value should be true")

    def test_negative(self):
        """Test that False raises an AssertionError."""
        with self.assertRaises(AssertionError):
            self.assertIs(True, False, "Value should not be true")

if __name__ == '__main__':
    unittest.main(verbosity=2)
