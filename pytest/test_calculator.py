"""
Module for testing the Calculator class.
"""

from calculator import Calculator
import pytest

@pytest.fixture
def calc():
    """Provides a Calculator instance."""
    return Calculator()

def test_addition(calculator_instance):
    """Test addition method."""
    assert calculator_instance.add(2, 3) == 5

def test_subtraction(calculator_instance):
    """Test subtraction method."""
    assert calculator_instance.subtract(5, 3) == 2

def test_multiplication(calculator_instance):
    """Test multiplication method."""
    assert calculator_instance.multiply(3, 4) == 12

def test_division(calculator_instance):
    """Test division method."""
    assert calculator_instance.divide(8, 2) == 4
def test_division_by_zero(calculator_instance):
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError):
        calculator_instance.divide(10, 0)
