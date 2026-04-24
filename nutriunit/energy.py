"""
nutriunit.energy

Energy-related helpers for nutrient-density calculations.
These functions provide simple, transparent calculations for
energy density and related transformations.
"""

def energy_density_kj_per_100g(kj: float, mass_g: float) -> float:
    """
    Compute energy density in kJ per 100 g.

    Example:
        energy_density_kj_per_100g(500, 50) -> 1000
    """
    if mass_g <= 0:
        raise ValueError("mass_g must be positive.")
    return (kj / mass_g) * 100


def energy_density_kcal_per_100g(kcal: float, mass_g: float) -> float:
    """
    Compute energy density in kcal per 100 g.

    Example:
        energy_density_kcal_per_100g(120, 60) -> 200
    """
    if mass_g <= 0:
        raise ValueError("mass_g must be positive.")
    return (kcal / mass_g) * 100
