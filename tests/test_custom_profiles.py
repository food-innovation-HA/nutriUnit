from nutriunit.custom_profiles import build_profile

def test_build_profile_encourage_only():
    profile = build_profile(encourage=["protein", "fibre"])
    assert profile["protein"] == 1.0
    assert profile["fibre"] == 1.0

def test_build_profile_limit_only():
    profile = build_profile(limit=["sodium", "sfa"])
    assert profile["sodium"] == -1.0
    assert profile["sfa"] == -1.0

def test_build_profile_with_weights_overrides_defaults():
    profile = build_profile(
        encourage=["protein"],
        limit=["sodium"],
        weights={"protein": 2.0, "sodium": -1.5},
    )
    assert profile["protein"] == 2.0
    assert profile["sodium"] == -1.5

def test_build_profile_with_base_profile_name():
    profile = build_profile(
        encourage=["protein"],
        base_profile="WHO_ADULT",
    )
    # base profile values should still be present
    assert "vitamin_a" in profile
    # and protein should be set/overridden by encourage
    assert profile["protein"] == 1.0
