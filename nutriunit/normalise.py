"""
nutriunit.normalise

Normalisation helpers for nutrient values.
These functions convert raw nutrient amounts into standardised bases
(e.g., per 100 g, per serving, per MJ), which is essential for
nutrient-density calculations and comparative assessments.
"""

def per_100g(value: float, mass_g: float) -> float:
    """
    Normalise a nutrient value to a per-100 g basis.

    Example:
        per_100g(12, 50) -> 24
    """
    if mass_g <= 0:
        raise ValueError("mass_g must be positive.")
    return (value / mass_g) * 100


def per_serving(value: float, serving_g: float) -> float:
    """
    Normalise a nutrient value to a per-serving basis.

    Example:
        per_serving(12, 150) -> 8
    """
    if serving_g <= 0:
        raise ValueError("serving_g must be positive.")
    return (value / serving_g)


def per_mj(value: float, energy_kj: float) -> float:
    """
    Normalise a nutrient value to a per-megajoule basis.

    Example:
        per_mj(12, 500) -> 24
    """
    if energy_kj <= 0:
        raise ValueError("energy_kj must be positive.")
    return (value / energy_kj) * 1000
