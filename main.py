import streamlit as st
import pickle
import pandas as pd

# ---------------------------
# Load the trained model
# ---------------------------
with open("models/linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("House Price Prediction")

st.write("Enter the house details below to predict its price.")

# ---------------------------
# User Inputs
# ---------------------------

bhk = st.slider("BHK", 1, 5, 3)
bathrooms = st.slider("Bathrooms", 1, 6, 3)
built_up_area = st.number_input("Built Up Area (sq ft)", min_value=300, value=1500)
carpet_area = st.number_input("Carpet Area (sq ft)", min_value=200, value=1200)
floor_number = st.number_input("Floor Number", min_value=0, max_value=40, value=5)
total_floors = st.number_input("Total Floors", min_value=1, max_value=45, value=12)
property_age = st.number_input("Property Age (years)", min_value=0, max_value=40, value=5)
parking_spaces = st.slider("Parking Spaces", 0, 5, 2)
security_score = st.slider("Security Score", 0.0, 10.0, 5.0)
distance_to_city_center = st.number_input("Distance to City Center (km)", min_value=0.0, value=10.0)
distance_to_metro = st.number_input("Distance to Metro (km)", min_value=0.0, value=2.0)

# ---------------------------
# Predict Button
# ---------------------------

if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "bhk": [bhk],
        "bathrooms": [bathrooms],
        "built_up_area": [built_up_area],
        "carpet_area": [carpet_area],
        "floor_number": [floor_number],
        "total_floors": [total_floors],
        "property_age": [property_age],
        "parking_spaces": [parking_spaces],
        "security_score": [security_score],
        "distance_to_city_center_km": [distance_to_city_center],
        "distance_to_metro_km": [distance_to_metro]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: {prediction[0]:.2f} Lakhs")
