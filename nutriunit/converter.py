"""
nutriunit.converter

Core unit conversion utilities for nutrient and energy values.
These functions are intentionally simple, predictable, and easy to test.
"""

# Mass conversions
def grams_to_milligrams(value: float) -> float:
    return value * 1000

def milligrams_to_grams(value: float) -> float:
    return value / 1000


# Energy conversions
def kcal_to_kj(value: float) -> float:
    return value * 4.184

def kj_to_kcal(value: float) -> float:
    return value / 4.184

from .food_item import FoodItem

def get_nutrient(food: FoodItem, nutrient: str):
    """
    Retrieve a nutrient value from a FoodItem using internal nutrient names.
    """
    return getattr(food, nutrient, None)
