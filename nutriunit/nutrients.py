"""
Canonical nutrient registry for nutriunit.

This defines the internal nutrient names used across the package.
"""

# Core macronutrients
NUTRIENTS = {
    "protein": "Protein (g)",
    "fat": "Fat (g)",
    "carbohydrate": "Carbohydrate (g)",
    "energy_kcal": "Energy (kcal) (kcal)",

    # Carbohydrate quality
    "total_sugars": "Total sugars (g)",
    "starch": "Starch (g)",
    "oligosaccharides": "Oligosaccharide (g)",

    # Fat quality
    "saturated_fat": "Satd FA /100g fd (g)",
    "monounsaturated_fat": "Mono FA /100g food (g)",
    "polyunsaturated_fat": "Poly FA /100g food (g)",
    "trans_fat": "Trans FAs /100g food (g)",
    "cholesterol_mg": "Cholesterol (mg)",

    # Minerals / misc
    "sodium": "Sodium (mg)",

    # Other
    "water": "Water (g)",
    "alcohol": "Alcohol (g)",
}
