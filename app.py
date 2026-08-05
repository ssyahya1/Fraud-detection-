import streamlit as st

st.set_page_config(
    page_title="Fraud Guard AI",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# logo image for expanded sidebar, icon_image for mobile/collapsed sidebar
st.logo(
    image="assets/logo.png",
    icon_image="assets/logo.png"
)

home_page = st.Page("pages/1_Home.py", title="Home", icon="🏠", default=True)
dashboard_page = st.Page("pages/2_Dashboard.py", title="Dashboard", icon="📊")
dataset_page = st.Page("pages/3_Dataset.py", title="Dataset", icon="📁")
prediction_page = st.Page("pages/4_Prediction.py", title="Prediction", icon="🔮")
about_page = st.Page("pages/5_About.py", title="About", icon="ℹ️")

pg = st.navigation([
    home_page,
    dashboard_page,
    dataset_page,
    prediction_page,
    about_page
])

pg.run()