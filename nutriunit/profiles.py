"""
nutriunit.profiles

Reference nutrient profiles (RDVs/DRVs/NRVs) for nutrient-density scoring.
Values are based on EU NRVs for adults (per day), which align with EFSA DRVs.
"""

#-------------------------------------------------------------
# EU NRV / DRV values for adults (mg unless otherwise stated)
#-------------------------------------------------------------

EU_NRV_ADULT = {
    # Vitamins
    "vitamin_a": 0.8,        # mg (800 mcg) 
    "vitamin_d": 0.005,      # mg (5 mcg) 
    "vitamin_e": 12,         # mg 
    "vitamin_k": 0.075,      # mg (75 mcg) 
    "vitamin_c": 80,         # mg 
    "thiamin": 1.1,          # mg (B1) 
    "riboflavin": 1.4,       # mg (B2) 
    "niacin": 16,            # mg (B3) 
    "vitamin_b6": 1.4,       # mg 
    "folate": 0.2,           # mg (200 mcg) 
    "vitamin_b12": 0.0025,   # mg (2.5 mcg) 
    "biotin": 0.05,          # mg (50 mcg) 
    "pantothenic_acid": 6,   # mg (B5) 

    # Minerals
    "calcium": 800,          # mg 
    "iron": 14,              # mg 
    "zinc": 10,              # mg 
    "iodine": 0.15,          # mg (150 mcg) 
    "selenium": 0.055,       # mg
    "fluoride": 3.5,
    "chloride": 800,

    # Macronutrients
    "protein": 50,
}

# ---------------------------------------------------------------------------
# WHO / Global Reference Profiles (public-domain summary values)
# ---------------------------------------------------------------------------

WHO_ADULT = {
    "vitamin_a": 0.7,
    "vitamin_c": 45,
    "vitamin_d": 0.005,
    "vitamin_e": 10,
    "thiamin": 1.1,
    "riboflavin": 1.1,
    "niacin": 14,
    "vitamin_b6": 1.3,
    "folate": 0.4,
    "vitamin_b12": 0.0024,
    "calcium": 1000,
    "iron": 14,
    "zinc": 11,
    "iodine": 0.15,
    "selenium": 0.055,
    "magnesium": 310,
    "protein": 50,
}

WHO_PREGNANT = {
    **WHO_ADULT,
    "iron": 27,
    "folate": 0.6,
    "iodine": 0.22,
    "protein": 71,
}

WHO_CHILD_1_3 = {
    "vitamin_a": 0.3,
    "vitamin_c": 15,
    "vitamin_d": 0.01,
    "vitamin_e": 6,
    "thiamin": 0.5,
    "riboflavin": 0.5,
    "niacin": 6,
    "vitamin_b6": 0.5,
    "folate": 0.15,
    "vitamin_b12": 0.0009,
    "calcium": 700,
    "iron": 7,
    "zinc": 3,
    "iodine": 0.09,
    "selenium": 0.02,
    "magnesium": 80,
    "protein": 13,
}

WHO_CHILD_4_8 = {
    "vitamin_a": 0.4,
    "vitamin_c": 25,
    "vitamin_d": 0.01,
    "vitamin_e": 7,
    "thiamin": 0.6,
    "riboflavin": 0.6,
    "niacin": 8,
    "vitamin_b6": 0.6,
    "folate": 0.2,
    "vitamin_b12": 0.0012,
    "calcium": 1000,
    "iron": 10,
    "zinc": 5,
    "iodine": 0.12,
    "selenium": 0.03,
    "magnesium": 130,
    "protein": 19,
}

UK_ADULT = {
    "vitamin_a": 0.7,
    "vitamin_c": 40,
    "vitamin_d": 0.01,
    "vitamin_e": 12,
    "thiamin": 1.0,
    "riboflavin": 1.3,
    "niacin": 16,
    "vitamin_b6": 1.4,
    "folate": 0.2,
    "vitamin_b12": 0.0015,
    "calcium": 700,
    "iron": 14,
    "zinc": 9.5,
    "iodine": 0.14,
    "selenium": 0.055,
    "magnesium": 300,
    "protein": 50,
}

KENYA_ADULT = {
    "vitamin_a": 0.6,
    "vitamin_c": 45,
    "vitamin_d": 0.005,
    "vitamin_e": 10,
    "thiamin": 1.0,
    "riboflavin": 1.1,
    "niacin": 14,
    "vitamin_b6": 1.3,
    "folate": 0.4,
    "vitamin_b12": 0.0024,
    "calcium": 1000,
    "iron": 18,
    "zinc": 12,
    "iodine": 0.15,
    "selenium": 0.055,
    "magnesium": 300,
    "protein": 50,
}

INDONESIA_ADULT = {
    "vitamin_a": 0.6,
    "vitamin_c": 75,
    "vitamin_d": 0.005,
    "vitamin_e": 15,
    "thiamin": 1.1,
    "riboflavin": 1.1,
    "niacin": 15,
    "vitamin_b6": 1.3,
    "folate": 0.4,
    "vitamin_b12": 0.0024,
    "calcium": 1000,
    "iron": 15,
    "zinc": 11,
    "iodine": 0.15,
    "selenium": 0.055,
    "magnesium": 300,
    "protein": 60,
}

ATHLETE_MODERATE = {
    **WHO_ADULT,
    "protein": 90,
    "iron": 18,
    "vitamin_b6": 1.7,
    "vitamin_b12": 0.003,
}

ATHLETE_ENDURANCE = {
    **WHO_ADULT,
    "protein": 110,
    "iron": 20,
    "vitamin_b6": 2.0,
    "vitamin_b12": 0.003,
}

ATHLETE_STRENGTH = {
    **WHO_ADULT,
    "protein": 130,
    "iron": 18,
    "vitamin_b6": 2.0,
    "vitamin_b12": 0.003,
}

PROFILE_REGISTRY = {
    "EU_ADULT": EU_NRV_ADULT,
    "WHO_ADULT": WHO_ADULT,
    "WHO_PREGNANT": WHO_PREGNANT,
    "WHO_CHILD_1_3": WHO_CHILD_1_3,
    "WHO_CHILD_4_8": WHO_CHILD_4_8,
    "UK_ADULT": UK_ADULT,
    "KENYA_ADULT": KENYA_ADULT,
    "INDONESIA_ADULT": INDONESIA_ADULT,
    "ATHLETE_MODERATE": ATHLETE_MODERATE,
    "ATHLETE_ENDURANCE": ATHLETE_ENDURANCE,
    "ATHLETE_STRENGTH": ATHLETE_STRENGTH,
}

def get_profile(name: str) -> dict:
    """
    Retrieve a reference nutrient profile by name.

    Parameters
    ----------
    name : str
        The profile identifier (e.g., "EU_ADULT").

    Returns
    -------
    dict
        The nutrient reference profile.

    Raises
    ------
    KeyError
        If the profile name is not recognised.
    """
    key = name.upper()
    if key not in PROFILE_REGISTRY:
        raise KeyError(f"Unknown nutrient profile: {name}")
    return PROFILE_REGISTRY[key]

def all_nutrients():
    """Return a sorted list of all nutrients across all registered profiles."""
    nutrients = set()
    for profile in PROFILE_REGISTRY.values():
        nutrients.update(profile.keys())
    return sorted(nutrients)

from .nutrients import NUTRIENTS

def list_available_nutrients():
    """
    Return the canonical list of nutrient names used internally.
    """
    return list(NUTRIENTS.keys())
