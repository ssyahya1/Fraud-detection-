# AI Fraud Detection System

## Overview

AI Fraud Detection System is a machine learning web application that detects fraudulent banking transactions in real time. The project combines data preprocessing, feature engineering, multiple machine learning algorithms, hyperparameter tuning, and an interactive Streamlit interface to provide accurate fraud predictions and insightful data visualizations.

---

## Features

- Real-time fraud prediction
- Interactive analytics dashboard
- Exploratory Data Analysis (EDA)
- Feature engineering and preprocessing
- Multiple machine learning models
- Hyperparameter tuning
- Automatic best model selection
- Interactive Plotly visualizations
- Dataset explorer
- Responsive Streamlit application

---

## Machine Learning Workflow

### Data Preprocessing

- Missing value analysis
- Duplicate detection
- Feature engineering
- Timestamp feature extraction
- Standard scaling
- One-Hot Encoding

### Imbalanced Data Handling

- SMOTE (Synthetic Minority Oversampling Technique)

### Models Implemented

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- Random Forest (GridSearchCV)
- Random Forest (RandomizedSearchCV)

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score

The best-performing model is automatically selected and saved for deployment.

---

## Exploratory Data Analysis

The project includes comprehensive EDA such as:

- Fraud distribution
- Transaction amount analysis
- Device type analysis
- Merchant category analysis
- Authentication method analysis
- Risk score analysis
- Correlation heatmap
- Feature importance
- Hourly fraud trends
- Numerical feature analysis
- Categorical feature analysis

---

## Project Structure

```text
Fraud Detection/
│
├── app.py
├── pages/
│   ├── 1_Home.py
│   ├── 2_Prediction.py
│   ├── 3_Dashboard.py
│   ├── 4_Dataset.py
│   └── 5_About.py
│
├── assets/
│   ├── logo.png
│   ├── bank_banner.jpg
│   ├── dashboard_header.jpg
│   ├── fraud.png
│   ├── legit.png
│   ├── ai_brain.jpg
│   └── cyber_security.jpg
│
├── fraud_detection_model.pkl
├── synthetic_fraud_dataset.csv
├── style.css
├── requirements.txt
└── README.md
```

---

## Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn
- Plotly

### Machine Learning

- Scikit-learn
- XGBoost
- Imbalanced-Learn (SMOTE)

### Deployment

- Streamlit

---

## Dashboard

The dashboard provides:

- Total transactions
- Fraud cases
- Fraud percentage
- Average transaction amount
- Fraud distribution
- Transaction trends
- Device analysis
- Merchant category analysis
- Risk score distribution
- Interactive visualizations

---

## Prediction Module

The application accepts transaction details including:

- Transaction Amount
- Transaction Type
- Merchant Category
- Device Type
- Location
- Account Balance
- Card Type
- Authentication Method
- Risk Score
- Card Age
- Previous Fraud Activity
- Daily Transaction Count
- Average Transaction Amount (7 Days)
- Transaction Distance
- Weekend Indicator

The trained machine learning model predicts whether a transaction is legitimate or fraudulent.

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Fraud-Detection-System.git
```

Navigate to the project directory

```bash
cd Fraud-Detection-System
```

Install the required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Screenshots

Include screenshots of:

- Home Page
- Prediction Page
- Dashboard
- Dataset Explorer
- About Page

---

## Future Improvements

- Real-time transaction monitoring
- Explainable AI (SHAP)
- Email notifications
- User authentication
- Cloud deployment
- Database integration
- REST API support

---

## Developer

**Syed Muhammad Yahya**

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## License

This project is licensed under the MIT License.