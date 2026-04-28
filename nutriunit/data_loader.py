from importlib.resources import files
import pandas as pd

# Step 1 loader
MW_CURATED_FILENAME = "mw2021_curated.parquet"

def load_mw_curated() -> pd.DataFrame:
    """
    Load the curated McCance & Widdowson 2021 dataset.
    """
    data_path = files("nutriunit.data") / MW_CURATED_FILENAME
    return pd.read_parquet(data_path)

from .mw_mapping import MW_TO_INTERNAL
from .food_item import FoodItem

def load_foods() -> dict[str, FoodItem]:
    """
    Load curated MW foods as a dictionary of FoodItem objects,
    keyed by food name for fast lookup and fuzzy search.
    """
    df = load_mw_curated()

    # Drop the two header rows MW includes
    df = df.iloc[2:].reset_index(drop=True)

    foods = {}

    for _, row in df.iterrows():
        kwargs = {
            "code": row["Food Code"],
            "name": row["Food Name"],
            "description": row["Description"],
            "group": row["Group"],
        }

        # Map nutrients
        for mw_col, internal in MW_TO_INTERNAL.items():
            if mw_col in row.index:
                kwargs[internal] = row[mw_col]

        item = FoodItem(**kwargs)
        foods[item.name] = item   # <-- KEY CHANGE

    return foods
