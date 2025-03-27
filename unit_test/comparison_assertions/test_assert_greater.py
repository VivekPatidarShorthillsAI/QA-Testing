"""
This module contains unit tests for comparison assertions using unittest.
"""

import unittest

class TestAssertGreaterEqual(unittest.TestCase):
    """
    Test cases for assertGreaterEqual method in unittest.
    """

    def test_positive(self):
        """
        Test cases where the first value is greater than or equal to the second.
        """
        self.assertGreaterEqual(
            6, 5,
            "First value should be greater than or equal to second"
        )
        self.assertGreaterEqual(
            5, 5,
            "First value should be greater than or equal to second"
        )

    def test_negative(self):
        """
        Test cases where the first value is not greater than or equal to the second.
        """
        with self.assertRaises(AssertionError):
            self.assertGreaterEqual(
                4, 5,
                "First value should not be greater than or equal to second"
            )

if __name__ == '__main__':
    unittest.main()
