import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="World Population Analysis",
    page_icon="🌍",
    layout="wide"
)

# Title
st.title("🌍 World Population Analysis Dashboard")

st.markdown("---")

# Introduction
st.header("📖 Introduction")

st.write("""
The **World Population Analysis** project explores global population trends using
data analysis and visualization techniques. The dataset contains information
about countries, their population, area, density, growth rate, and other
demographic indicators.

This project applies **Data Cleaning, Exploratory Data Analysis (EDA), and
Visualization** to discover meaningful insights from the data.
""")

# Objectives
st.header("🎯 Objectives")

st.markdown("""
- Analyze the world population dataset.
- Clean and preprocess the data.
- Perform Exploratory Data Analysis (EDA).
- Identify the most and least populated countries.
- Analyze population density across countries.
- Visualize population trends using interactive charts.
- Answer research questions using data-driven insights.
""")

# Technologies Used
st.header("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Programming
    - Python

    ### Libraries
    - Pandas
    - NumPy
    - Matplotlib
    - Plotly Express
    """)

with col2:
    st.markdown("""
    ### Framework
    - Streamlit

    ### Tools
    - Jupyter Notebook
    - VS Code
    - GitHub
    """)

# Project Workflow
st.header("📊 Project Workflow")

st.markdown("""
1. Dataset Collection
2. Data Cleaning
3. Data Preprocessing
4. Exploratory Data Analysis (EDA)
5. Data Visualization
6. Research Questions
7. Conclusion
""")

# Features
st.header("✨ Features")

st.markdown("""
✅ Interactive Dashboard

✅ Clean Dataset View

✅ Data Cleaning Process

✅ Exploratory Data Analysis

✅ Population Visualizations

✅ Research Question Analysis

✅ Final Conclusion
""")

# Dataset Information
st.header("📂 Dataset Information")

st.info("""
**Dataset Name:** World Population Dataset

The dataset includes information such as:

- Country
- Continent
- Population
- Area (km²)
- Density
- Growth Rate
- World Population Percentage
- Rank
""")

# Navigation
st.header("📌 Dashboard Navigation")

st.success("""
Use the **sidebar** to navigate between the pages:

🏠 Home

📂 Dataset

🧹 Data Cleaning

📊 EDA

❓ Research Questions

✅ Conclusion
""")

st.markdown("---")

# Footer
st.caption("Developed using Python, Pandas, Plotly Express, Matplotlib, and Streamlit")