from nutriunit.profiles import PROFILE_REGISTRY, get_profile
import pytest

def test_all_profiles_load():
    """Every profile in the registry should load and return a non-empty dict."""
    for name in PROFILE_REGISTRY:
        profile = get_profile(name)
        assert isinstance(profile, dict)
        assert len(profile) > 0

def test_profile_lookup_is_case_insensitive():
    """Profile names should load regardless of case."""
    for name in PROFILE_REGISTRY:
        lower = name.lower()
        assert get_profile(lower) == PROFILE_REGISTRY[name]

def test_unknown_profile_raises_keyerror():
    """Unknown profile names should raise a clear KeyError."""
    with pytest.raises(KeyError):
        get_profile("NOT_A_REAL_PROFILE")
