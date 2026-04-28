nutriUnit — Nutrient Functional Unit Builder

A lightweight, flexible tool for exploring nutrient density models using McCance & Widdowson data.

nutriUnit is a small, research‑friendly application designed to help users build, test, and compare nutrient functional units. It supports both predefined nutrient density models and fully custom scoring profiles, making it useful for teaching, exploratory analysis, and early‑stage methodological development.

This version (v0.2) focuses on clarity, transparency, and ease of experimentation rather than prescribing a single “correct” nutrient metric.
✨ Key Features (v0.2)
1. Custom nutrient profiles

Select nutrients to encourage or limit, assign weights, and optionally start from a population‑level base profile.
2. Predefined scoring models

Includes several commonly used nutrient density frameworks:

    NRF9(.3)
    LIM3
    Priority Micronutrient Value (PMV)
    UK Nutritional Index (ASF)
    “None” (fully custom)

These models act as templates — users can modify them freely.
3. Fuzzy food search

Search the McCance & Widdowson dataset using approximate matching (e.g., “app” → “Apple, raw”).
4. Nutrient composition viewer

Displays the full nutrient profile (per 100 g) for any selected food.
5. Radar chart visualisation

Interactive Plotly radar chart showing the nutrient “shape” of the selected food.
6. Nutrient density scoring

Compute a simple ratio‑based nutrient density score using your constructed profile.
7. Score breakdown

See how each nutrient contributes to the final score, including a bar chart for quick interpretation.
8. CSV export

Download a structured CSV containing:

    selected food
    nutrient composition
    constructed profile
    weights
    final score

Useful for teaching, reproducibility, and downstream analysis.
🧠 How it works (in brief)

nutriUnit builds a nutrient profile by combining:

    encourage nutrients (positive weights)
    limit nutrients (negative weights)
    optional base profiles (currently placeholders)

The scoring method is intentionally simple:
Code

score = Σ ( food_nutrient / reference_value )

This is not intended as a final or authoritative nutrient density metric — it’s a transparent starting point for exploring how different assumptions influence results.
📦 Installation
Code

pip install -r requirements.txt

Ensure you have Plotly installed for visualisation:
Code

pip install plotly

▶️ Running the app
Code

streamlit run app.py

The app will open in your browser at:
Code

http://localhost:8501

🗺️ Roadmap

Planned for v0.3 and beyond:

    fully populated WHO/FAO base profiles
    normalisation options
    multi‑food comparison
    improved nutrient filtering
    optional energy adjustment
    exportable plots

👥 Contributors

Developed at Harper Adams University as part of ongoing work on nutrient functional units, sustainability metrics, and teaching tools.

Contributions, suggestions, and issue reports are warmly welcomed.
