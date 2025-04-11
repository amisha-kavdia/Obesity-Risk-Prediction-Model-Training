import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("obesity_levels.pkl")

st.title("Obesity Level Predictor")
st.markdown("Predict your obesity level based on lifestyle and body metrics.")

st.header("📝 Enter Your Information")

# Collect inputs
age = st.number_input("Age", 1, 100, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
height = st.number_input("Height (in meters)", format="%.2f")
weight = st.number_input("Weight (in kg)", format="%.2f")

bmi = weight / (height ** 2) if height > 0 else 0  # Calculate BMI

activity_index = st.slider("Physical Activity Index (1 = low, 5 = high)", 1, 5)
physical_activity = st.slider("Hours of Physical Activity per Week", 0, 20)
technology_usage = st.slider("Daily Tech Use (hours)", 0, 16)
overweight_family_history = st.selectbox("Overweight in Family History?", ["Yes", "No"])
food_btw_meals = st.selectbox("Food Between Meals", ["No", "Sometimes", "Frequently", "Always"])
alcohol = st.selectbox("Alcohol Consumption", ["Never", "Sometimes", "Frequently"])
eat_veggies = st.selectbox("Do you eat vegetables daily?", ["Yes", "No"])
main_meals_count = st.slider("Number of Main Meals Per Day", 1, 5)
transportation = st.selectbox("Transportation Mode", ["Walking", "Bike", "Public", "Car"])
healthy_eating = st.selectbox("Do you follow healthy eating habits?", ["Yes", "No"])
water_glass = st.slider("Glasses of Water per Day", 0, 20)
monitoring_calories = st.selectbox("Do you monitor calorie intake?", ["Yes", "No"])
smoke = st.selectbox("Do you smoke?", ["Yes", "No"])

# Encode categorical variables
gender = 1 if gender == "Male" else 0
overweight_family_history = 1 if overweight_family_history == "Yes" else 0
eat_veggies = 1 if eat_veggies == "Yes" else 0
healthy_eating = 1 if healthy_eating == "Yes" else 0
monitoring_calories = 1 if monitoring_calories == "Yes" else 0
smoke = 1 if smoke == "Yes" else 0

# Map string inputs to numerical categories
food_map = {"No": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
alcohol_map = {"Never": 0, "Sometimes": 1, "Frequently": 2}
transport_map = {"Walking": 0, "Bike": 1, "Public": 2, "Car": 3}

food_btw_meals = food_map[food_btw_meals]
alcohol = alcohol_map[alcohol]
transportation = transport_map[transportation]

# Input features array
input_data = np.array([[bmi, weight, age, gender, activity_index, technology_usage,
                        overweight_family_history, food_btw_meals, alcohol, eat_veggies,
                        main_meals_count, height, transportation, physical_activity,
                        healthy_eating, water_glass, monitoring_calories, smoke]])

if st.button("Predict Obesity Level"):
    prediction = model.predict(input_data)[0]
    st.subheader("📊 Prediction:")
    st.success(f"Your predicted obesity level is: **{prediction}**")
