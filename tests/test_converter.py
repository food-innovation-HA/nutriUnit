from nutriunit.converter import grams_to_milligrams, milligrams_to_grams

def test_roundtrip():
    assert milligrams_to_grams(grams_to_milligrams(1.0)) == 1.0
