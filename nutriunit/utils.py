"""
nutriunit.utils

Shared utility functions used across the nutriunit package.
These helpers keep core modules clean and avoid repeated boilerplate.
"""

def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """
    Divide numerator by denominator, returning a default value if the
    denominator is zero or negative.

    This is useful for nutrient-density calculations where missing or
    zero values can otherwise cause noisy failures.

    Example:
        safe_divide(10, 0) -> 0.0
    """
    if denominator <= 0:
        return default
    return numerator / denominator


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Clamp a value to a specified range.

    Example:
        clamp(12, 0, 10) -> 10
    """
    return max(min_value, min(value, max_value))


def validate_positive(value: float, name: str = "value") -> None:
    """
    Raise a ValueError if a value is not positive.

    Example:
        validate_positive(-5, "mass_g") -> ValueError
    """
    if value <= 0:
        raise ValueError(f"{name} must be positive.")
