"""Module for testing mathematical operations."""

import math

def test_check_floor():
    """Test if math.floor works correctly."""
    num = 6
    assert num == math.floor(6.34532)

def check_equal():
    """Check equality of two numbers."""
    assert 50 == 50  # Corrected constant comparison

def test_check_difference():
    """Test the difference between two numbers."""
    assert 99 - 43 == 56  # Corrected the expected value

def check_square_root():
    """Check if the square root is calculated correctly."""
    val = 9
    assert val == math.sqrt(81)
