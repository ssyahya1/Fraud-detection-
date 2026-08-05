import streamlit as st
import pandas as pd

st.header("📁 Dataset Explorer")

@st.cache_data
def load_data():
    return pd.read_csv('synthetic_fraud_dataset.csv')

try:
    df = load_data()
    
    st.subheader("Dataset Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Duplicate Rows", df.duplicated().sum())

    st.subheader("Data Preview")
    st.dataframe(df.head(100), use_container_width=True)

    st.subheader("Null Values & Schema")
    null_info = pd.DataFrame({
        "Data Type": df.dtypes,
        "Null Count": df.isnull().sum()
    })
    st.dataframe(null_info, use_container_width=True)

except Exception as e:
    st.error(f"Error loading synthetic_fraud_dataset.csv: {e}")