"""
This module contains a function to reverse text and its corresponding test.
"""

def reverse_text(text):
    """
    Reverses the given text string.
    """
    return text[::-1]

def test_reverse_text():
    """
    Tests the reverse_text function with a sample input.
    """
    assert reverse_text('python') == 'nohtyp'
    