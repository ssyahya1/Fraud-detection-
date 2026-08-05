import streamlit as st

st.header("ℹ️ About & Pipeline Details")

st.markdown("""
### Model Pipeline Architecture
1. **ColumnTransformer**:
   - `StandardScaler()` applied to numerical features.
   - `OneHotEncoder(drop='first')` applied to categorical variables.
2. **Resampling**:
   - `SMOTE` oversampling applied within the cross-validation pipeline step.
3. **Classifiers Evaluated**:
   - Logistic Regression
   - Decision Tree Classifier
   - Random Forest Classifier
   - XGBoost Classifier
   - RandomizedSearchCV & GridSearchCV Hyperparameter Optimization

### File Structure
- `app.py`: Entry point for Streamlit application UI.
- `pages/`: Automated multi-page layout directory.
- `fraud_detection_model.pkl`: Serialized model pipeline artifact.
""")