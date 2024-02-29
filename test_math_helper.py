# test_math_helper.py
from math_helper import add, subtract, multiply, divide, power, factorial
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_power():
    assert power(2, 3) == 8
    assert power(2, 0) == 1

def test_divide_error():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)