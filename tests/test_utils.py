from nutriunit.utils import safe_divide, clamp, validate_positive
import pytest

def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5

def test_safe_divide_zero():
    assert safe_divide(10, 0) == 0.0

def test_clamp():
    assert clamp(12, 0, 10) == 10
    assert clamp(-3, 0, 10) == 0
    assert clamp(5, 0, 10) == 5

def test_validate_positive():
    validate_positive(5)  # should not raise
    with pytest.raises(ValueError):
        validate_positive(0)
