from nutriunit.energy import (
    energy_density_kj_per_100g,
    energy_density_kcal_per_100g,
)

def test_energy_density_kj():
    assert energy_density_kj_per_100g(500, 50) == 1000

def test_energy_density_kcal():
    assert energy_density_kcal_per_100g(120, 60) == 200
