import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Fraud Detection App")
st.write("Enter transaction details to check for fraud")

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Example inputs - replace with your actual features
amount = st.number_input("Transaction Amount", min_value=0.0)
time = st.number_input("Time", min_value=0.0)

if st.button("Check for Fraud"):
    # Put your actual prediction code here
    input_data = np.array([[time, amount]]) # Replace with your features
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    
    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction Looks Safe")
