"""Module for testing assertLessEqual functionality using unittest."""

import unittest

class TestAssertLessEqual(unittest.TestCase):
    """Test cases for assertLessEqual assertions."""

    def test_positive(self):
        """Test cases where the first value is less than or equal to the second."""
        self.assertLessEqual(4, 5, "First value should be less than or equal to second")
        self.assertLessEqual(5, 5, "First value should be less than or equal to second")

    def test_negative(self):
        """Test cases where the first value is not less than or equal to the second."""
        with self.assertRaises(AssertionError):
            self.assertLessEqual(6, 5, "First value should not be less than or equal to second")

if __name__ == '__main__':
    unittest.main()
