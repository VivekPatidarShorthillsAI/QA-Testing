"""Module for testing mathematical operations."""

import math

def test_check_difference(input_value):
    """Test to check the difference between two numbers."""
    assert 99 - 93 == input_value

def test_check_square_root(input_value):
    """Test to check the square root of a number."""
    assert input_value == math.sqrt(64)
