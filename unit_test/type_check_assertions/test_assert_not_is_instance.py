"""
This module contains unit tests for verifying the behavior of assertNotIsInstance.
"""

import unittest

class TestClass:
    """
    A simple class used for testing purposes.
    """
    def method_one(self):
        """A placeholder public method."""
    def method_two(self):
        """Another placeholder public method."""

class TestAssertNotIsInstance(unittest.TestCase):
    """
    Unit tests for assertNotIsInstance assertions.
    """
    def test_positive(self):
        """
        Test that an object is not an instance of TestClass.
        """
        obj = "not a TestClass"
        self.assertNotIsInstance(obj, TestClass, "Object should not be instance of TestClass")

    def test_negative(self):
        """
        Test that an AssertionError is raised when an object is an instance of TestClass.
        """
        obj = TestClass()
        with self.assertRaises(AssertionError):
            self.assertNotIsInstance(obj, TestClass, "Object should be instance of TestClass")

if __name__ == '__main__':
    unittest.main()
