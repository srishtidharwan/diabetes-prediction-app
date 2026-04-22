import streamlit as st
import joblib
import numpy as np

# Model load karo
model = joblib.load("diabetes_model.pkl")

st.title("🩺 Diabetes Prediction App")
st.write("Fill Your details Here !")

# User se input lo
pregnancies = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 300, 120)
blood_pressure = st.number_input("Blood Pressure", 0, 200, 70)
skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 1, 120, 25)

# Predict button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])
    result = model.predict(input_data)
    
    if result[0] == 1:
        st.error("There may be  possibility of having  Diabetes ⚠️")
    else:
        st.success("✅Congrats! No Diabetes ")