import streamlit as st

# Configure page settings and browser tab icon using your local asset
st.set_page_config(
    page_title="Fraud Guard AI",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Display your local custom logo at the top of the sidebar navigation menu
st.logo("assets/logo.png")

# Define page routes matching your exact folder file paths
home_page = st.Page("pages/1_Home.py", title="Home", icon="🏠", default=True)
dashboard_page = st.Page("pages/2_Dashboard.py", title="Dashboard", icon="📊")
dataset_page = st.Page("pages/3_Dataset.py", title="Dataset", icon="📁")
prediction_page = st.Page("pages/4_Prediction.py", title="Prediction", icon="🔮")
about_page = st.Page("pages/5_About.py", title="About", icon="ℹ️")

# Build navigation bar in exact requested order
pg = st.navigation([
    home_page,
    dashboard_page,
    dataset_page,
    prediction_page,
    about_page
])

# Execute current page route
pg.run()