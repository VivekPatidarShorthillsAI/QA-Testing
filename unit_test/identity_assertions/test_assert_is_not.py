"""Test cases for assertIsNot unittest method."""
import unittest


class TestAssertIsNot(unittest.TestCase):
    """Test class for assertIsNot functionality."""

    def test_positive(self):
        """Test that different objects are not identical."""
        list_a = [1, 2, 3]
        list_b = [1, 2, 3]
        self.assertIsNot(list_a, list_b)

    def test_negative(self):
        """Test that identical objects raise AssertionError."""
        list_a = [1, 2, 3]
        list_b = list_a
        with self.assertRaises(AssertionError):
            self.assertIsNot(list_a, list_b)


if __name__ == '__main__':
    unittest.main()
    