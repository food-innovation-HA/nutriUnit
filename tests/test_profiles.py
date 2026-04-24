from nutriunit.profiles import EU_NRV_ADULT

def test_profile_contains_key_nutrients():
    assert "vitamin_c" in EU_NRV_ADULT
    assert "iron" in EU_NRV_ADULT
    assert "protein" in EU_NRV_ADULT

def test_profile_values_are_positive():
    for value in EU_NRV_ADULT.values():
        assert value > 0
