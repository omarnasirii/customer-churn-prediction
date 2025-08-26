import streamlit as st
import pandas as pd
import pickle
import os

st.title("Customer Churn Predictor")

# Load trained model, scaler, and feature names
base_dir = os.path.dirname(__file__)
model_path = os.path.join(base_dir, "../models/logreg_model.pkl")
scaler_path = os.path.join(base_dir, "../models/scaler.pkl")
features_path = os.path.join(base_dir, "../models/feature_names.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)
with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)
with open(features_path, "rb") as f:
    feature_names = pickle.load(f)

# Example input fields (customize as needed)
tenure = st.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total_charges = st.number_input("Total Charges", 0.0, 9000.0, 1000.0)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

# Create a DataFrame with only the continuous features for scaling
continuous_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
df_to_scale = pd.DataFrame([[tenure, monthly_charges, total_charges]], columns=continuous_cols)

# Scale the continuous features
scaled_continuous = scaler.transform(df_to_scale)

# Create the full input DataFrame for the model, initialized with zeros
input_df = pd.DataFrame(columns=feature_names)
input_df.loc[0] = 0

# Populate the DataFrame with user inputs (scaled and categorical)
input_df.loc[0, 'tenure'] = scaled_continuous[0, 0]
input_df.loc[0, 'MonthlyCharges'] = scaled_continuous[0, 1]
input_df.loc[0, 'TotalCharges'] = scaled_continuous[0, 2]
if contract == "One year":
    input_df.loc[0, 'Contract_One year'] = 1
elif contract == "Two year":
    input_df.loc[0, 'Contract_Two year'] = 1
# Add other user inputs here if you expand the app

prediction = model.predict(input_df)

if prediction[0] == 1:
    st.error("⚠️ This customer is likely to churn.")
else:
    st.success("✅ This customer is unlikely to churn.")
