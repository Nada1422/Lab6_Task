import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Provides a Calculator instance for testing."""
    return Calculator()


def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(2.5, 2.5) == 5.0


def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2
    assert calc.subtract(0, 0) == 0


def test_multiply(calc):
    assert calc.multiply(4, 3) == 12
    assert calc.multiply(5, 0) == 0
    assert calc.multiply(-2, 3) == -6


def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 2) == 2.5
    
    # Test division by zero exception
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(5, 0)


def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(9, 0.5) == 3.0
