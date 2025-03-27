"""
This module contains unit tests for comparison assertions using unittest.
"""

import unittest

class TestAssertLess(unittest.TestCase):
    """
    Test cases for the assertLess method in unittest.
    """

    def test_positive(self):
        """
        Test that assertLess passes when the first value is less than the second.
        """
        self.assertLess(4, 5, "First value should be less than second")

    def test_negative(self):
        """
        Test that assertLess raises an AssertionError when the first value is not less 
        than the second.
        """
        with self.assertRaises(AssertionError):
            self.assertLess(6, 5, "First value should not be less than second")

if __name__ == '__main__':
    unittest.main()
