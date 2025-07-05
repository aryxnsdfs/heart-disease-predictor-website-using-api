import streamlit as st
import pickle
import numpy as np

# Load your trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Heart Disease Predictor")

# All 13 required inputs
age = st.number_input("Age", min_value=0, max_value=120)
sex = st.selectbox("Sex (1 = male, 0 = female)", [1, 0])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", min_value=0)
chol = st.number_input("Cholesterol", min_value=0)
fbs = st.selectbox("Fasting Blood Sugar > 120? (1 = yes, 0 = no)", [1, 0])
restecg = st.selectbox("Rest ECG (0 = normal, 1 = ST-T abnormality, 2 = LVH)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", min_value=0)
exang = st.selectbox("Exercise Induced Angina (1 = yes, 0 = no)", [1, 0])
oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, format="%.1f")
slope = st.selectbox("Slope (0 = up, 1 = flat, 2 = down)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thal (3 = normal, 6 = fixed, 7 = reversible)", [3, 6, 7])

# Predict button
if st.button("Predict"):
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                          thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("⚠️ High risk of heart disease")
    else:
        st.success("✅ Low risk of heart disease")
