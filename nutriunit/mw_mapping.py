"""
Mapping from MW column names to nutriunit internal nutrient names.
"""

from .nutrients import NUTRIENTS

MW_TO_INTERNAL = {v: k for k, v in NUTRIENTS.items()}
