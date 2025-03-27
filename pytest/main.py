"""
This module contains test cases for verifying the behavior of math functions.
It uses pytest to test the math.floor() and math.sqrt() functions.
"""

import math
import pytest

@pytest.mark.parametrize("test_input, output", [(5.234, 5), (9.99, 10), (0.456, 0), (7.905, 7)])
def test_floor(test_input, output):
    """
    Test the math.floor() function to ensure it rounds down the input correctly.

    Parameters:
    test_input (float): The value to apply math.floor to.
    output (int): The expected result of math.floor(test_input).
    """
    assert output == math.floor(test_input)

@pytest.mark.parametrize(
    "val, result",
    [
        (8, 2.8284271247461903),
        (1, 1.0),
        (3, 1.7320508075688772),
        (5, 2.23606797749979),
    ],
)
def test_square_root(val, result):
    """
    Test the math.sqrt() function to ensure it computes the square root correctly.

    Parameters:
    val (int): The value to calculate the square root of.
    result (float): The expected result of math.sqrt(val).
    """
    assert result == math.sqrt(val)
