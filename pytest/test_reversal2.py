"""
This module contains a function to reverse text and its corresponding test cases.
"""

import pytest

def reverse_text(text):
    """
    Reverses the given string.

    Args:
        text (str): The string to reverse.

    Returns:
        str: The reversed string.

    Raises:
        ValueError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise ValueError('Expected a string')
    return text[::-1]

def test_reverse_text_non_string():
    """
    Tests that reverse_text raises a ValueError when the input is not a string.
    """
    with pytest.raises(ValueError):
        reverse_text(1234)
