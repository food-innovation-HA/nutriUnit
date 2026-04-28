from dataclasses import dataclass
from typing import Optional

@dataclass
class FoodItem:
    code: str
    name: str
    description: str
    group: str

    # Nutrients (all optional because MW sometimes has missing values)
    protein: Optional[float] = None
    fat: Optional[float] = None
    carbohydrate: Optional[float] = None
    energy_kcal: Optional[float] = None

    total_sugars: Optional[float] = None
    starch: Optional[float] = None
    oligosaccharides: Optional[float] = None

    saturated_fat: Optional[float] = None
    monounsaturated_fat: Optional[float] = None
    polyunsaturated_fat: Optional[float] = None
    trans_fat: Optional[float] = None
    cholesterol_mg: Optional[float] = None

    water: Optional[float] = None
    alcohol: Optional[float] = None
