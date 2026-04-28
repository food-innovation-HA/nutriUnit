from nutriunit.profiles import get_profile
from .utils import safe_divide, validate_positive

def to_float(value, default=0.0):
    """
    Convert MW nutrient values to float safely.
    Handles 'Tr', 'None', 'nan', empty strings, and numeric strings.
    """
    if value is None:
        return default

    if isinstance(value, (int, float)):
        return float(value)

    if isinstance(value, str):
        v = value.strip().lower()

        # MW trace values
        if v in ("tr", "trace"):
            return 0.0

        # Missing or invalid values
        if v in ("none", "nan", "", "n/a"):
            return default

        try:
            return float(v)
        except ValueError:
            return default

    return default


def score(nutrient_profile, reference_profile, method="ratio"):
    """
    Compute nutrient density score for a food.

    Parameters
    ----------
    nutrient_profile : dict
        Nutrient composition of the food.
    reference_profile : dict or str
        Either a nutrient reference profile dictionary,
        or the name of a profile registered in PROFILE_REGISTRY.
    method : str
        Scoring method (currently only "ratio" is implemented).

    Returns
    -------
    float
        The nutrient density score.
    """

    # Allow profile names
    if isinstance(reference_profile, str):
        reference_profile = get_profile(reference_profile)

    if not isinstance(reference_profile, dict):
        raise TypeError("reference_profile must be a dict or a registered profile name")

    if method != "ratio":
        raise ValueError(f"Unsupported scoring method: {method}")

    score_components = []

    for nutrient, raw_value in nutrient_profile.items():
        if nutrient not in reference_profile:
            continue

        # Convert MW values safely
        value = to_float(raw_value, default=0.0)

        ref_value = reference_profile[nutrient]
        validate_positive(ref_value, name=f"reference value for {nutrient}")

        ratio = safe_divide(value, ref_value, default=0.0)
        score_components.append(ratio)

    return sum(score_components)
