"""
nutriunit.density

A simple, extensible nutrient-density scoring engine.

This module provides a minimal scoring function that compares a food's
nutrient profile to a reference profile. The default method is a
ratio-based score, but the design allows for future expansion to
threshold-based scoring, weighting schemes, and uncertainty propagation.
"""

from .utils import safe_divide, validate_positive


def score(
    nutrient_profile: dict,
    reference_profile: dict,
    method: str = "ratio",
) -> float:
    """
    Compute a nutrient-density score.

    Parameters
    ----------
    nutrient_profile : dict
        A mapping of nutrient name -> amount in the food item.
    reference_profile : dict
        A mapping of nutrient name -> recommended or reference amount.
    method : str
        Scoring method. Currently supports:
            - "ratio": sum(food / reference) across shared nutrients.

    Returns
    -------
    float
        A nutrient-density score (higher = more nutrient-dense).

    Notes
    -----
    - Only nutrients present in BOTH profiles are used.
    - Missing nutrients are ignored rather than penalised.
    - safe_divide ensures stable behaviour when reference values are zero.
    """

    if method != "ratio":
        raise ValueError(f"Unsupported scoring method: {method}")

    score_components = []

    for nutrient, value in nutrient_profile.items():
        if nutrient not in reference_profile:
            continue

        ref_value = reference_profile[nutrient]

        validate_positive(ref_value, name=f"reference value for {nutrient}")

        ratio = safe_divide(value, ref_value, default=0.0)
        score_components.append(ratio)

    return sum(score_components)
