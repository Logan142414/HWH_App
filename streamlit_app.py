import streamlit as st
import pickle
import numpy as np

# --- Load saved model ---
with open("xgb_model.pkl", "rb") as f:
    model = pickle.load(f)

# --- Streamlit App Layout ---
st.set_page_config(page_title="Probability Predictor", layout="centered")
st.title("Probability Predictor")

st.write("Use the sliders below to set your inputs:")

# --- Input sliders (customize ranges based on your model features) ---
features = []
for i in range(1, 11):
    val = st.slider(f"Feature {i}", min_value=1, max_value=5, step=1)
    features.append(val)

# --- Predict ---
if st.button("Predict Probability"):
    input_array = np.array([features])  # Shape = (1, 10)
    prob = model.predict_proba(input_array)[0][1]  # Probability for class 1
    st.success(f"Predicted Probability: {prob:.2%}")
