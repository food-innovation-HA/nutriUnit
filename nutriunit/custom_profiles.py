from nutriunit.profiles import get_profile

BASE_PROFILES = {
    None: {},
    "WHO_ADULT": {},
    "WHO_PREGNANT": {},
    "KENYA_ADULT": {},
    "INDONESIA_ADULT": {},
}

def build_profile(encourage=None, limit=None, weights=None, base_profile=None):
    profile = {}

    # Start from base profile if it exists
    if base_profile in BASE_PROFILES:
        profile.update(BASE_PROFILES[base_profile])

    # Add encourage/limit/weights
    if encourage:
        for n in encourage:
            profile[n] = weights.get(n, 1.0)

    if limit:
        for n in limit:
            profile[n] = weights.get(n, -1.0)

    return profile
