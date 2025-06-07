import streamlit as st

# Title
st.title("BMI (Body Mass Index) Calculator")

# Description
st.write("This app calculates your **Body Mass Index (BMI)** based on your height and weight.")

# User inputs
name = st.text_input("Enter your name")
weight = st.number_input("Enter your weight (in kilograms)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (in meters)", min_value=0.5, max_value=2.5, format="%.2f")

# Calculate BMI when button is clicked
if st.button("Calculate BMI"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"{name}, your BMI is: {bmi:.2f}")
        
        # Interpretation
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.info("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Height must be greater than 0.")
