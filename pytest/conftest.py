"""
This module contains pytest fixtures for testing.
"""

import pytest

@pytest.fixture
def input_value():
    """Fixture that provides an input value."""
    value = 8
    return value
