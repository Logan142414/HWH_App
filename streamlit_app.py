import streamlit as st
import pickle
import numpy as np
import pandas as pd

# --- Load saved model. Preview Period ---
with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Load saved model. Graduation ---
#with open("xgb_model.pkl", "rb") as f:
    #modelgrad = pickle.load(f)


# --- Streamlit App Layout ---
st.set_page_config(page_title="Predicting Graduation/Preview Period", layout="centered")

# --- Top row with Elon and HWH logos ---
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.image("elon_logo.png", width=120)

with col2:
    st.markdown("<h2 style='text-align: center; margin-top: 15px;'>Predicting Graduation/Preview Period</h2>", unsafe_allow_html=True)

with col3:
    st.image("HWH_logo.png", width=120)

# --- Subtitle below the header ---
st.subheader("Made By Elon University")


st.write("Use the buttons below to choose a value:")

# --- Input sliders (customize ranges based on your model features) ---

feature_names = [
    "adult_education", "child_care", "community", "employment", "housing",
    "income", "math_skills", "mental_health", "reading_skills", "social", "substance_abuse"
]

# --- Streamlit radio buttons for each feature ---
features = []
with st.expander("SSF scores (1-5)",expanded=True):
    for name in feature_names:
        val = st.radio(
            f"{name.replace('_', ' ').title()}",
            options=[1, 2, 3, 4, 5],
            index=2,  # default is 3
            horizontal=True  # optional: makes it more compact
        )
        features.append(val)

featureSSF = ['ssf_initial:adult_education', 'ssf_initial:child_care',
       'ssf_initial:community', 'ssf_initial:employment',
       'ssf_initial:housing', 'ssf_initial:income', 'ssf_initial:math_skills',
       'ssf_initial:mental_health', 'ssf_initial:reading_skills',
       'ssf_initial:social', 'ssf_initial:substance_abuse']

# --- Predict ---


#if st.button("Predict Probability for Passing Preview Period (>12)"):
   # input_df = pd.DataFrame([features], columns=featureSSF)
   # prob = model.predict_proba(input_df)[0][1]
   # if prob > 0.8:
       # st.success(f"High chance of passing preview: {prob:.2%}")
   # elif prob > 0.4:
       # st.warning(f"Moderate chance of passing preview: {prob:.2%}")
   # else:
   #     st.error(f"Low chance of passing preview: {prob:.2%}")


#if st.button("Predict Probability for Graduation"):
   # input_df = pd.DataFrame([features], columns=featureSSF)
    #prob = modelgrad.predict_proba(input_df)[0][1]
    #if prob > 0.8:
        #st.success(f"High chance of graduation: {prob:.2%}")
    #elif prob > 0.4:
        #st.warning(f"Moderate chance of graduation: {prob:.2%}")
    #else:
        #st.error(f"Low chance of graduation: {prob:.2%}")


if st.button("Predict Probabilities"):
    input_df = pd.DataFrame([features], columns=featureSSF)

    # --- Preview Period Prediction ---
    prob_preview = model.predict_proba(input_df)[0][1]
    st.markdown("### 📊 Preview Period Prediction")
    if prob_preview > 0.8:
        st.success(f"High chance of passing preview: {prob_preview:.2%}")
    elif prob_preview > 0.4:
        st.warning(f"Moderate chance of passing preview: {prob_preview:.2%}")
    else:
        st.error(f"Low chance of passing preview: {prob_preview:.2%}")

    # --- Graduation Prediction ---
    prob_grad = model.predict_proba(input_df)[0][1]
    st.markdown("### 🎓 Graduation Prediction")
    if prob_grad > 0.8:
        st.success(f"High chance of graduating: {prob_grad:.2%}")
    elif prob_grad > 0.4:
        st.warning(f"Moderate chance of graduating: {prob_grad:.2%}")
    else:
        st.error(f"Low chance of graduating: {prob_grad:.2%}")



