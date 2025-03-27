"""This module contains sample test cases for pytest."""

import math

def test_check_difference():
    """Test to check the difference between two numbers."""
    assert 99 - 43 == 56

def test_check_square_root():
    """Test to check the square root of a number."""
    val = 8
    assert val == math.sqrt(64)
