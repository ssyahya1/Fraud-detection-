import streamlit as st
import pandas as pd
import joblib

st.header("🔮 Real-Time Fraud Prediction")

@st.cache_resource
def load_model():
    return joblib.load("fraud_detection_model.pkl")

try:
    model = load_model()
    st.success("Model pipeline loaded successfully!")
except Exception as e:
    st.error(f"Failed to load 'fraud_detection_model.pkl': {e}")
    st.stop()

st.subheader("Enter Transaction Attributes")

with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        risk_score = st.number_input("Risk Score", min_value=0.0, max_value=100.0, value=15.0, step=0.1)
        account_balance = st.number_input("Account Balance ($)", min_value=0.0, value=5000.0, step=100.0)
        transaction_amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=250.0, step=10.0)
        avg_tx_7d = st.number_input("Avg Transaction Amount (7d)", min_value=0.0, value=150.0, step=10.0)
        daily_tx_count = st.number_input("Daily Transaction Count", min_value=0, value=3, step=1)
        card_age = st.number_input("Card Age (Days/Months)", min_value=0, value=365, step=1)

    with col2:
        tx_distance = st.number_input("Transaction Distance", min_value=0.0, value=12.5, step=0.1)
        merchant_cat = st.selectbox("Merchant Category", ["Retail", "Online", "Travel", "Electronics", "Groceries", "Other"])
        tx_type = st.selectbox("Transaction Type", ["Online", "POS", "ATM", "Transfer"])
        auth_method = st.selectbox("Authentication Method", ["PIN", "OTP", "Biometric", "None"])
        device_type = st.selectbox("Device Type", ["Mobile", "Desktop", "Tablet", "Other"])
        card_type = st.selectbox("Card Type", ["Visa", "Mastercard", "Amex", "Discover"])

    with col3:
        location = st.selectbox("Location / Country", ["US", "UK", "CA", "IN", "AU", "Other"])
        ip_flag = st.selectbox("IP Address Flag", [0, 1], format_func=lambda x: "High Risk IP (1)" if x == 1 else "Normal IP (0)")
        prev_fraud = st.selectbox("Previous Fraudulent Activity", [0, 1], format_func=lambda x: "Yes (1)" if x == 1 else "No (0)")
        date_input = st.date_input("Transaction Date")
        time_input = st.time_input("Transaction Time")

    submitted = st.form_submit_button("Analyze Transaction")

if submitted:
    # 1. Temporal Feature Extraction
    dt = pd.to_datetime(f"{date_input} {time_input}")
    
    hour = dt.hour
    day = dt.day
    month = dt.month
    day_of_week = dt.dayofweek
    is_weekend = 1 if day_of_week >= 5 else 0

    # 2. Complete DataFrame matching x_train features exactly
    input_data = pd.DataFrame([{
        "Risk_Score": risk_score,
        "Account_Balance": account_balance,
        "Transaction_Amount": transaction_amount,
        "Avg_Transaction_Amount_7d": avg_tx_7d,
        "Daily_Transaction_Count": daily_tx_count,
        "Transaction_Distance": tx_distance,
        "Card_Age": card_age,
        "Merchant_Category": merchant_cat,
        "Transaction_Type": tx_type,
        "Authentication_Method": auth_method,
        "Device_Type": device_type,
        "Card_Type": card_type,
        "Location": location,
        "IP_Address_Flag": ip_flag,
        "Previous_Fraudulent_Activity": prev_fraud,
        "Hour": hour,
        "Day": day,
        "Month": month,
        "Day_of_Week": day_of_week,
        "Is_Weekend": is_weekend
    }])

    # 3. Predict via Pipeline
    try:
        prediction = model.predict(input_data)[0]
        prediction_prob = model.predict_proba(input_data)[0][1]

        st.markdown("---")
        st.subheader("Prediction Result")

        res_col1, res_col2 = st.columns(2)

        with res_col1:
            if prediction == 1:
                st.error("🚨 **FRAUD DETECTED**")
            else:
                st.success("✅ **TRANSACTION IS LEGITIMATE**")

        with res_col2:
            st.metric(
                label="Fraud Risk Score",
                value=f"{prediction_prob * 100:.2f}%"
            )

        st.progress(float(prediction_prob))

    except Exception as err:
        st.error(f"Prediction Error: {err}")