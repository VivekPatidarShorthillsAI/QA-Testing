"""
This module contains a sample function and its test case.
"""

import pytest

def func(x):
    """
    Adds 5 to the input value.
    """
    return x + 5

def test_method():
    """
    Tests the func function with a sample input.
    """
    assert func(3) == 8
