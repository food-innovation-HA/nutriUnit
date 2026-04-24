from nutriunit.converter import (
    grams_to_milligrams,
    milligrams_to_grams,
    kcal_to_kj,
    kj_to_kcal,
)

def test_mass_roundtrip():
    assert milligrams_to_grams(grams_to_milligrams(1.0)) == 1.0

def test_energy_roundtrip():
    assert abs(kj_to_kcal(kcal_to_kj(1.0)) - 1.0) < 1e-9
