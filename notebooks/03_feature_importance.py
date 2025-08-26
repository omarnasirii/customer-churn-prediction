import pandas as pd
import shap
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("../data/preprocessed_telco.csv")
X = df.drop("Churn_Yes", axis=1)
y = df["Churn_Yes"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)
shap.summary_plot(shap_values[1], X)
