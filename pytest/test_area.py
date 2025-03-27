"""Module for testing area calculations."""

import area

# Test cases for area calculations
class TestArea:
    """Test suite for area module."""

    def test_circle(self):
        """Test the area of a circle."""
        assert area.circle(14) == 615.44

    def test_square(self):
        """Test the area of a square."""
        assert area.square(4) == 16

    def test_rectangle(self):
        """Test the area of a rectangle."""
        assert area.rectangle(6, 9) == 54

    def test_parallelogram(self):
        """Test the area of a parallelogram."""
        assert area.parallelogram(7, 5) == 35

    def test_triangle(self):
        """Test the area of a triangle."""
        assert area.triangle(12, 10) == 60
