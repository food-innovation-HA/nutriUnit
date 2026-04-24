import streamlit as st
from nutriunit import build_profile, score, all_nutrients

# Pull all nutrients dynamically from the package
nutrients = all_nutrients()

st.set_page_config(page_title="nutriUnit", layout="wide")

st.title("nutriUnit – Custom Nutrient Functional Unit")

st.markdown(
    "Define your own nutrient functional unit by selecting nutrients to "
    "encourage or limit, optionally starting from a population profile, "
    "and adjusting nutrient weights."
)

# --- Layout ---
criteria_col, food_col = st.columns(2)

# =========================
# 1. Criteria / profile side
# =========================
with criteria_col:
    st.header("1. Choose nutrient criteria")

    base_profile = st.selectbox(
        "Base profile (optional)",
        ["None", "WHO_ADULT", "WHO_PREGNANT", "KENYA_ADULT", "INDONESIA_ADULT"],
    )

    if base_profile == "None":
        base_profile = None

    encourage = st.multiselect(
    "Nutrients to encourage",
    nutrients,
    default=[],
)

    limit = st.multiselect(
    "Nutrients to limit",
    nutrients,
    default=[],
)

    st.subheader("Adjust nutrient weights")

    weights = {}

    if encourage:
        st.markdown("**Weights for encouraged nutrients (positive):**")
        for n in encourage:
            weights[n] = st.slider(
                f"{n.replace('_', ' ').title()} (encourage)",
                min_value=0.0,
                max_value=5.0,
                value=1.0,
                step=0.1,
            )

    if limit:
        st.markdown("**Weights for limited nutrients (negative):**")
        for n in limit:
            # store as negative internally
            w = st.slider(
                f"{n.replace('_', ' ').title()} (limit)",
                min_value=0.0,
                max_value=5.0,
                value=1.0,
                step=0.1,
            )
            weights[n] = -w

    # Build profile preview
    profile = build_profile(
        encourage=encourage,
        limit=limit,
        weights=weights if weights else None,
        base_profile=base_profile,
    )

    st.subheader("Constructed nutrient profile")
    st.json(profile)

# =========================
# 2. Food side
# =========================
with food_col:
    st.header("2. Enter food composition (per 100 g)")

    food = {}
    for nutrient in nutrients:
        food[nutrient] = st.number_input(
            nutrient.replace("_", " ").title(),
            min_value=0.0,
            value=0.0,
            step=0.1,
        )

    st.header("3. Compute score")

    if st.button("Compute nutrient density score"):
        result = score(food, profile)
        st.success(f"Nutrient density score: **{result:.3f}**")
