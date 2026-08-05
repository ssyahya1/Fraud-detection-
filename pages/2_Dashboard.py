import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.header("📊 Data Visualizations & Analytics")

@st.cache_data
def load_data():
    df = pd.read_csv('synthetic_fraud_dataset.csv')
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df["Hour"] = df["Timestamp"].dt.hour
    df["Day_of_Week"] = df["Timestamp"].dt.dayofweek
    df["Is_Weekend"] = (df["Day_of_Week"] >= 5).astype(int)
    return df

try:
    df = load_data()
    
    st.subheader("Target Distribution")
    fig, ax = plt.subplots(figsize=(6, 3))
    sns.countplot(data=df, x='Fraud_Label', palette='Set2', ax=ax)
    st.pyplot(fig)

    st.subheader("Feature Correlation Matrix")
    num_df = df.select_dtypes(include=['float64', 'int64'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(num_df.corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
    st.pyplot(fig)

except Exception as e:
    st.error(f"Error loading dataset: {e}")