## nutriUnit

A small, practical toolkit for nutrient‑unit conversions and nutrient‑density calculations.

nutriUnit provides a straightforward Python interface for converting nutrient units, normalising values, and preparing data for nutrient‑density scoring. It is designed to support teaching, research, and reproducible food‑systems modelling, without the overhead of a full nutrition‑analysis framework.

## Features

    Unit conversions (e.g. grams ↔  milligrams, kilocalories ↔  kilojoules)
    Normalisation helpers (per 100 g, per serving, per MJ)
    Simple nutrient‑density scoring primitives
    A composable API suitable for LCA, nutrition modelling, and teaching
    Tested, version‑controlled, and packaged using modern Python standards

## Installation

Development installation:

git clone git@github.com:food-innovation-HA/nutriUnit.git
cd nutriUnit
pip install -e .[dev]

# PyPI installation will be available once the package reaches its first release.

## Quick Start

from nutriunit import converter as nu

nu.grams_to_milligrams(2.5)   # 2500
nu.milligrams_to_grams(750)   # 0.75

## Planned functionality:

from nutriunit import density
density.score(food_item, reference_profile="EFSA")

## Roadmap

    [ ] Full nutrient‑conversion matrix
    [ ] Nutrient‑density scoring module
    [ ] Uncertainty‑propagation hooks
    [ ] Example notebooks for teaching
    [ ] Documentation site (MkDocs)
    [ ] GitHub Actions CI
    [ ] PyPI release

## Contributing

Contributions are welcome.
For substantial changes, please open an issue to discuss the proposal first.

## License

MIT License.
