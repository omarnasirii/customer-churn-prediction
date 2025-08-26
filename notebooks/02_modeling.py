import pandas as pd
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

# Load preprocessed data
df = pd.read_csv("../data/preprocessed_telco.csv")
X = df.drop("Churn_Yes", axis=1)
y = df["Churn_Yes"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Define continuous columns and fit scaler only on them
continuous_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
scaler = StandardScaler()

# Fit on training data and transform
X_train[continuous_cols] = scaler.fit_transform(X_train[continuous_cols])
X_test[continuous_cols] = scaler.transform(X_test[continuous_cols])

# Train logistic regression
model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)
preds = model.predict(X_test)

print(classification_report(y_test, preds))
print(confusion_matrix(y_test, preds))

# Save model, scaler, and feature names
os.makedirs("../models", exist_ok=True)
with open("../models/logreg_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("../models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)
with open("../models/feature_names.pkl", "wb") as f:
    pickle.dump(list(X.columns), f)
