import streamlit as st

st.header("📌 Project Overview")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Model Architecture", value="Random Forest / XGBoost")
with col2:
    st.metric(label="Data Preprocessing", value="SMOTE + Standard Scaling")
with col3:
    st.metric(label="Primary Metric Target", value="ROC-AUC Optimization")

st.markdown("---")

st.subheader("Key Features")
st.markdown("""
- **Automated Feature Engineering**: Extracts temporal features (`Hour`, `Day`, `Month`, `Day_of_Week`, `Is_Weekend`) directly from transaction timestamps.
- **Imbalance Handling**: Integrated Synthetic Minority Over-sampling Technique (SMOTE) inside `imblearn.pipeline.Pipeline` to prevent data leakage.
- **Categorical Encoding**: Scalable OneHotEncoding with first-category drop for numerical consistency.
""")