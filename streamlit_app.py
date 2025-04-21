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
st.title("Predicting Graduation/Preview Period")
st.subheader("Made By Elon University")
st.image("elon_logo.png", width=120)

st.write("Use the sliders below to set your inputs:")

# --- Input sliders (customize ranges based on your model features) ---

feature_names = [
    "adult_education", "child_care", "community", "employment", "housing",
    "income", "math_skills", "mental_health", "reading_skills", "social", "substance_abuse"
]

# --- Streamlit radio buttons for each feature ---
features = []
with st.expander("Adjust Your Survey Scores", expanded=True):
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


if st.button("Predict Probability for Passing Preview Period (>12)"):
    input_df = pd.DataFrame([features], columns=featureSSF)
    prob = model.predict_proba(input_df)[0][1]
    if prob > 0.8:
        st.success(f"High chance of passing preview: {prob:.2%}")
    elif prob > 0.4:
        st.warning(f"Moderate chance of passing preview: {prob:.2%}")
    else:
        st.error(f"Low chance of passing preview: {prob:.2%}")


#if st.button("Predict Probability for Graduation"):
   # input_df = pd.DataFrame([features], columns=featureSSF)
    #prob = modelgrad.predict_proba(input_df)[0][1]
    #if prob > 0.8:
        #st.success(f"High chance of graduation: {prob:.2%}")
    #elif prob > 0.4:
        #st.warning(f"Moderate chance of graduation: {prob:.2%}")
    #else:
        #st.error(f"Low chance of graduation: {prob:.2%}")
