"""
This module provides a simple calculator class for basic arithmetic operations.
"""

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the division of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
    