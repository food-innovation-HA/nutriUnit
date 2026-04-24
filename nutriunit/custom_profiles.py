from nutriunit.profiles import get_profile

def build_profile(
    encourage=None,
    limit=None,
    weights=None,
    base_profile=None,
):
    """
    Construct a custom nutrient profile for scoring.

    Parameters
    ----------
    encourage : list of str
        Nutrients to encourage (positive contribution).
    limit : list of str
        Nutrients to limit (negative contribution).
    weights : dict
        Optional explicit weights for specific nutrients.
    base_profile : str or dict
        Optional starting profile (e.g. "WHO_ADULT").

    Returns
    -------
    dict
        A nutrient profile mapping nutrient -> weight.
    """

    # Start from a base profile if provided
    if base_profile is not None:
        if isinstance(base_profile, str):
            profile = get_profile(base_profile).copy()
        elif isinstance(base_profile, dict):
            profile = base_profile.copy()
        else:
            raise TypeError("base_profile must be a dict or a registered profile name")
    else:
        profile = {}

    # Default lists
    encourage = encourage or []
    limit = limit or []
    weights = weights or {}

    # Apply encouragement (positive weights)
    for nutrient in encourage:
        profile[nutrient] = weights.get(nutrient, 1.0)

    # Apply limits (negative weights)
    for nutrient in limit:
        profile[nutrient] = weights.get(nutrient, -1.0)

    # Apply explicit weights (override)
    for nutrient, w in weights.items():
        profile[nutrient] = w

    return profile
