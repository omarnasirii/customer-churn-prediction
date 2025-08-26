# Customer Churn Prediction & Dashboard

![Python](https://img.shields.io/badge/Python-3.7%2B-blue) 
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange) 
![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-red)

A machine learning project that predicts customer churn for telecommunications companies and provides an interactive dashboard for business insights.

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Dataset](#-dataset)
- [Technical Details](#-technical-details)
- [Business Applications](#-business-applications)
- [Customization](#-customization)
- [Contributing](#-contributing)
- [Support](#-support)

---

## Project Overview
This project leverages a Logistic Regression model to predict customer churn and provides a Streamlit dashboard to visualize churn risk and explore scenarios interactively.

---

## 🏗️ Project Structure
Customer-Churn-Prediction/
├── app/
│   ├── streamlit_app.py                 # Interactive dashboard
│   └── data/
│       ├── preprocessed_telco.csv       # Cleaned data
│       └── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Original dataset
├── models/
│   ├── feature_names.pkl                # Feature names
│   ├── logreg_model.pkl                 # Trained model
│   └── scaler.pkl                       # Feature scaler
├── notebooks/
│   ├── 01_data_exploration.py           # Data preprocessing
│   ├── 02_modeling.py                   # Model training
│   └── 03_feature_importance.py         # Feature analysis
├── venv/                                # Virtual environment
├── .gitignore
└── README.md

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ (64-bit)
- Git

### Installation
1. **Create virtual environment**
   
python -m venv venv

2. **Activate (Windows PowerShell)**
   
venv\Scripts\Activate.ps1

3. **Install dependencies**
   
pip install --upgrade pip
pip install pandas scikit-learn matplotlib seaborn shap streamlit

4. **Prepare data and train model**
   
cd notebooks
python 01_data_exploration.py
python 02_modeling.py

5. **Run dashboard**
   
cd ../app
streamlit run streamlit_app.py

The dashboard will open at http://localhost:8501

## 📊 Usage
The dashboard allows you to:

- Input customer parameters (tenure, charges, contract type)

- Get instant churn predictions

- Test different scenarios

- View risk assessment (✅ Low risk / ⚠️ High risk)

## 🔍 Dataset
Telco Customer Churn Dataset (Kaggle)

- 7,043 customer records

- 21 features including demographics, services, and account information

- Target variable: Churn (Yes/No)

Key features:

- Demographic information

- Service subscriptions

- Account details

- Billing information

## ⚙️ Technical Details
Machine Learning Model:

- Algorithm: Logistic Regression

- Accuracy: 80-82%

- Preprocessing: One-hot encoding, feature scaling

- Validation: Stratified train-test split

## Key Features:

- Automated data pipeline

- Model persistence with pickle

- SHAP feature importance

- Interactive Streamlit interface

## 💡 Business Applications
- Customer Retention: Identify at-risk customers

- Service Optimization: Understand churn drivers

- Resource Allocation: Focus retention efforts

- Strategic Planning: Inform product decisions

## 🛠️ Customization
To adapt for your data:

- Replace dataset in app/data/

- Modify preprocessing in 01_data_exploration.py

- Adjust features in Streamlit app

- Retrain model with your data

## 📞 Support
Common issues:

- Ensure 64-bit Python is used

- Verify all dependencies are installed

- Confirm virtual environment is activated

- Check model files are generated before running dashboard

