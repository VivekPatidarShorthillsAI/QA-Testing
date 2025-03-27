"""
Unit tests for assertIsNotNone method in unittest.
"""

import unittest

class TestAssertIsNotNone(unittest.TestCase):
    """
    Test cases for assertIsNotNone method.
    """

    def test_positive(self):
        """
        Test that assertIsNotNone passes when the value is not None.
        """
        self.assertIsNotNone("not None", "Value should not be None")

    def test_negative(self):
        """
        Test that assertIsNotNone raises an AssertionError when the value is None.
        """
        with self.assertRaises(AssertionError):
            self.assertIsNotNone(None, "Value should be None")

if __name__ == '__main__':
    unittest.main()
