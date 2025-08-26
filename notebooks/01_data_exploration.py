import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("../data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Explore data
print(df.head())
print(df.isnull().sum())
print(df['Churn'].value_counts(normalize=True))

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Encode categorical variables
df_encoded = pd.get_dummies(df.drop(['customerID'], axis=1), drop_first=True)

# Scale continuous features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_encoded[['tenure', 'MonthlyCharges', 'TotalCharges']] = scaler.fit_transform(
    df_encoded[['tenure', 'MonthlyCharges', 'TotalCharges']]
)

# Save preprocessed data
df_encoded.to_csv("../data/preprocessed_telco.csv", index=False)
