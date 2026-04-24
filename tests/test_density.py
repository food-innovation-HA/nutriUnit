from nutriunit.density import score
import pytest


def test_basic_ratio_scoring():
    food = {"protein": 10, "iron": 2}
    ref = {"protein": 5, "iron": 1}
    assert score(food, ref) == (10/5) + (2/1)


def test_missing_nutrients_are_ignored():
    food = {"protein": 10}
    ref = {"protein": 5, "iron": 1}
    assert score(food, ref) == 10/5


def test_zero_reference_raises():
    food = {"protein": 10}
    ref = {"protein": 0}
    with pytest.raises(ValueError):
        score(food, ref)
