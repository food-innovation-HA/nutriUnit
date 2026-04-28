import difflib
import streamlit as st
from nutriunit import build_profile, score, load_foods
from nutriunit.profiles import list_available_nutrients
from nutriunit.converter import get_nutrient

# -----------------------------
# Session state initialisation
# -----------------------------
if "selected_food" not in st.session_state:
    st.session_state.selected_food = None

if "encourage" not in st.session_state:
    st.session_state.encourage = []

if "limit" not in st.session_state:
    st.session_state.limit = []

if "weights" not in st.session_state:
    st.session_state.weights = {}

if "base_profile" not in st.session_state:
    st.session_state.base_profile = None

if "last_score" not in st.session_state:
    st.session_state.last_score = None

if "predefined_model" not in st.session_state:
    st.session_state.predefined_model = "None"


# -----------------------------
# Helper: fuzzy food search
# -----------------------------
def search_foods(query, foods, limit=20):
    if not query:
        return list(foods.items())[:limit]

    names = list(foods.keys())
    matches = difflib.get_close_matches(query, names, n=limit, cutoff=0.0)
    return [(name, foods[name]) for name in matches]


# -----------------------------
# Load data
# -----------------------------
nutrients = list_available_nutrients()
foods = load_foods()

st.set_page_config(page_title="nutriUnit", layout="wide")
st.title("nutriUnit – Custom Nutrient Functional Unit")

st.markdown(
    "Define your own nutrient functional unit by selecting nutrients to "
    "encourage or limit, optionally starting from a population profile, "
    "and adjusting nutrient weights."
)

criteria_col, food_col = st.columns(2)

# =========================
# 1. Criteria / profile side
# =========================
with criteria_col:
    st.header("1. Choose nutrient criteria")

    # -----------------------------
    # Pre-defined scoring systems
    # -----------------------------
    predefined_models = {
        "None": {
            "base": None,
            "encourage": [],
            "limit": [],
            "weights": {}
        },
        "NRF9.3": {
            "base": None,
            "encourage": [
                "protein", "fibre", "vitamin_a", "vitamin_c", "vitamin_e",
                "calcium", "iron", "magnesium", "potassium"
            ],
            "limit": ["saturated_fat", "added_sugars", "sodium"],
            "weights": {}
        },
        "NRF9 LIM3": {
            "base": None,
            "encourage": [
                "protein", "fibre", "vitamin_a", "vitamin_c", "vitamin_e",
                "calcium", "iron", "magnesium", "potassium"
            ],
            "limit": ["saturated_fat", "added_sugars", "sodium"],
            "weights": {}
        },
        "Priority Micronutrient Value (PMV)": {
            "base": None,
            "encourage": [
                "iron", "zinc", "vitamin_a", "folate",
                "vitamin_b12", "calcium", "riboflavin"
            ],
            "limit": [],
            "weights": {}
        },
        "UK Nutritional Index (ASF)": {
            "base": None,
            "encourage": [
                "iron", "zinc", "vitamin_b12", "riboflavin",
                "iodine", "calcium"
            ],
            "limit": ["saturated_fat", "sodium"],
            "weights": {}
        }
    }

    model_name = st.selectbox(
        "Pre-defined nutrient density model",
        list(predefined_models.keys()),
        index=list(predefined_models.keys()).index(
            st.session_state.predefined_model
        )
    )
    st.session_state.predefined_model = model_name

    model = predefined_models[model_name]

    # -----------------------------
    # Base profile
    # -----------------------------
    base_profile = model["base"]
    if base_profile is None:
        base_profile = st.selectbox(
            "Base profile (optional)",
            ["None", "WHO_ADULT", "WHO_PREGNANT", "KENYA_ADULT", "INDONESIA_ADULT"],
            index=(
                ["None", "WHO_ADULT", "WHO_PREGNANT", "KENYA_ADULT", "INDONESIA_ADULT"]
                .index(st.session_state.base_profile)
                if st.session_state.base_profile in
                   ["None", "WHO_ADULT", "WHO_PREGNANT", "KENYA_ADULT", "INDONESIA_ADULT"]
                else 0
            )
        )
        if base_profile == "None":
            base_profile = None

    st.session_state.base_profile = base_profile

    # -----------------------------
    # Encourage nutrients
    # -----------------------------
    default_encourage = (
        model["encourage"]
        if model_name != "None"
        else st.session_state.encourage
    )

    encourage = st.multiselect(
        "Nutrients to encourage",
        nutrients,
        default=default_encourage,
    )
    st.session_state.encourage = encourage

    # -----------------------------
    # Limit nutrients
    # -----------------------------
    default_limit = (
        model["limit"]
        if model_name != "None"
        else st.session_state.limit
    )

    limit = st.multiselect(
        "Nutrients to limit",
        nutrients,
        default=default_limit,
    )
    st.session_state.limit = limit

    # -----------------------------
    # Weights
    # -----------------------------
    st.subheader("Adjust nutrient weights")

    weights = {}

    if encourage:
        st.markdown("**Weights for encouraged nutrients (positive):**")
        for n in encourage:
            weights[n] = st.slider(
                f"{n.replace('_', ' ').title()} (encourage)",
                min_value=0.0,
                max_value=5.0,
                value=st.session_state.weights.get(n, 1.0),
                step=0.1,
            )

    if limit:
        st.markdown("**Weights for limited nutrients (negative):**")
        for n in limit:
            w = st.slider(
                f"{n.replace('_', ' ').title()} (limit)",
                min_value=0.0,
                max_value=5.0,
                value=abs(st.session_state.weights.get(n, -1.0)),
                step=0.1,
            )
            weights[n] = -w

    st.session_state.weights = weights

    # -----------------------------
    # Build profile
    # -----------------------------
    profile = build_profile(
        encourage=encourage,
        limit=limit,
        weights=weights if weights else None,
        base_profile=base_profile,
    )

    st.subheader("Constructed nutrient profile")
    st.json(profile)

    # -----------------------------
    # Reset all settings
    # -----------------------------
    st.markdown("---")
    if st.button("Reset all settings"):
        st.session_state.selected_food = None
        st.session_state.encourage = []
        st.session_state.limit = []
        st.session_state.weights = {}
        st.session_state.base_profile = None
        st.session_state.last_score = None
        st.session_state.predefined_model = "None"

        st.experimental_rerun()

# =========================
# 2. Food side
# =========================
with food_col:
    st.header("2. Select a food from McCance & Widdowson")

    query = st.text_input("Search for a food")
    results = search_foods(query, foods)

    names = [name for name, _ in results]

    default_index = (
        names.index(st.session_state.selected_food)
        if st.session_state.selected_food in names
        else 0
    )

    food_name = st.selectbox("Select a food", names, index=default_index)
    selected_food = foods[food_name]
    st.session_state.selected_food = food_name

    st.subheader("Nutrient composition (per 100 g)")
    for nutrient in nutrients:
        value = get_nutrient(selected_food, nutrient)
        st.write(f"{nutrient.replace('_', ' ').title()}: {value}")
    # -----------------------------
    # Radar chart of nutrient composition
    # -----------------------------
    st.subheader("Nutrient radar chart")

    import plotly.graph_objects as go
    import numpy as np

    # Prepare data
    radar_values = [get_nutrient(selected_food, n) for n in nutrients]

    # Close the loop for radar chart
    radar_values.append(radar_values[0])
    radar_labels = nutrients + [nutrients[0]]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=radar_values,
        theta=[n.replace("_", " ").title() for n in radar_labels],
        fill='toself',
        name=food_name,
        line=dict(color='green')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, linewidth=1, gridcolor="lightgrey"),
        ),
        showlegend=True,
        height=500,
    )

    st.plotly_chart(fig, use_container_width=True)


    st.header("3. Compute score")

    if st.session_state.last_score is not None:
        st.info(f"Last score: **{st.session_state.last_score:.3f}**")

    if st.button("Compute nutrient density score"):
        food_dict = {n: get_nutrient(selected_food, n) for n in nutrients}
        result = score(food_dict, profile)
        st.session_state.last_score = result
        st.success(f"Nutrient density score: **{result:.3f}**")

    # -----------------------------
    # Score breakdown panel
    # -----------------------------
    st.subheader("Score breakdown")

    # Only compute breakdown if we have a score
    if st.session_state.last_score is not None:

        # Compute per-nutrient contributions
        contributions = []
        for n in nutrients:
            value = get_nutrient(selected_food, n)
            weight = st.session_state.weights.get(n, 0)
            contributions.append((n, value * weight))

        # Sort by absolute contribution (largest first)
        contributions.sort(key=lambda x: abs(x[1]), reverse=True)

        # Display table
        st.markdown("### Nutrient contributions")
        st.write(
            {
                "Nutrient": [n for n, _ in contributions],
                "Contribution": [round(c, 4) for _, c in contributions],
            }
        )

        # Bar chart
        st.markdown("### Contribution chart")
        import pandas as pd

        df = pd.DataFrame(
            {
                "nutrient": [n for n, _ in contributions],
                "contribution": [c for _, c in contributions],
            }
        )

        st.bar_chart(df, x="nutrient", y="contribution")

    # -----------------------------
    # CSV Export
    # -----------------------------
    st.subheader("Export results")

    if st.button("Download CSV"):
        import csv
        import io

        buffer = io.StringIO()
        writer = csv.writer(buffer)

        writer.writerow(["nutriUnit Export"])
        writer.writerow([])

        writer.writerow(["Selected food", food_name])
        writer.writerow([])

        writer.writerow(["Nutrient composition (per 100 g)"])
        writer.writerow(["Nutrient", "Value"])
        for nutrient in nutrients:
            writer.writerow([nutrient, get_nutrient(selected_food, nutrient)])
        writer.writerow([])

        writer.writerow(["Constructed nutrient profile"])
        writer.writerow(["Encourage nutrients"] + st.session_state.encourage)
        writer.writerow(["Limit nutrients"] + st.session_state.limit)
        writer.writerow([])

        writer.writerow(["Weights"])
        writer.writerow(["Nutrient", "Weight"])
        for n, w in st.session_state.weights.items():
            writer.writerow([n, w])
        writer.writerow([])

        writer.writerow(["Last nutrient density score", st.session_state.last_score])

        st.download_button(
            label="Download CSV",
            data=buffer.getvalue(),
            file_name="nutriunit_export.csv",
            mime="text/csv",
        )

st.markdown("---")
st.markdown("**nutriUnit v0.2** — Harper Adams University")
st.markdown("GitHub: https://github.com/food-innovation-HA-team/nutriUnit")
