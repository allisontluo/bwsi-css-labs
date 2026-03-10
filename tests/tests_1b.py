"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator

def test_addition():
    assert simple_calculator("add", 5, 3) == 8          # Test for positive numbers
    assert simple_calculator("add", -2, 2) == 0         # Test for negative and positive number
    assert simple_calculator("add", 0, 0) == 0          # Test for zero addition

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2     # Test for positive numbers
    assert simple_calculator("subtract", -2, -2) == 0   # Test for negative numbers
    assert simple_calculator("subtract", 0, 5) == -5    # Test for zero minuend

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15    # Test for positive numbers
    assert simple_calculator("multiply", -2, 2) == -4   # Test for negative and positive number
    assert simple_calculator("multiply", 0, 100) == 0   # Test for multiplication by zero

def test_division():
    assert simple_calculator("divide", 6, 3) == 2       # Test for positive numbers
    assert simple_calculator("divide", -4, 2) == -2     # Test for negative and positive number
    assert simple_calculator("divide", 5, 2) == 2.5     # Test for division resulting in float

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)               # Test division by zero

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("modulus", 5, 3)              # Test for invalid operation
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("", 5, 3)                     # Test for empty operation

def test_addition_edge_cases():
    assert simple_calculator("add", 1000000, 2000000) == 3000000
    assert simple_calculator("add", 3.5, 2.5) == 6.0
    assert simple_calculator("add", -7, -8) == -15

def test_subtraction_edge_cases():
    assert simple_calculator("subtract", 10, 10) == 0
    assert simple_calculator("subtract", 3.5, 1.2) == 2.3
    assert simple_calculator("subtract", -5, 4) == -9

def test_multiplication_edge_cases():
    assert simple_calculator("multiply", -3, -2) == 6
    assert simple_calculator("multiply", 2.5, 4) == 10.0
    assert simple_calculator("multiply", 1, 999) == 999

def test_division_edge_cases():
    assert simple_calculator("divide", -9, -3) == 3
    assert simple_calculator("divide", 0, 5) == 0
    assert simple_calculator("divide", 7.5, 2.5) == 3.0

if __name__ == "__main__":
    pytest.main()