import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="World Population Analysis",
    page_icon="🌍",
    layout="wide"
)

# Load Dataset
df = pd.read_csv("World Population Data.csv")

# Sidebar
st.sidebar.title("🌍 World Population Analysis")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Dataset",
        "Data Cleaning",
        "EDA",
        "Research Questions",
        "Conclusion"
    ]
)

# =====================================
# HOME PAGE
# =====================================
# =====================================
# HOME PAGE
# =====================================
if page == "Home":

    st.title("🌍 World Population Analysis Dashboard")

    st.markdown("---")

    # Introduction
    st.header("📖 Introduction")

    st.write("""
    The **World Population Analysis Dashboard** is an interactive web application
    developed using **Python** and **Streamlit**. This project analyzes the World
    Population dataset to understand population trends, country-wise population,
    density, area, growth rate, and other demographic information.

    The dashboard provides an easy way to explore the dataset through tables,
    charts, and statistical analysis.
    """)

    st.markdown("---")

    # Objectives
    st.header("🎯 Objectives")

    st.markdown("""
    - Analyze the World Population dataset.
    - Understand country-wise population statistics.
    - Compare population density and geographical area.
    - Perform Data Cleaning and Preprocessing.
    - Create interactive visualizations.
    - Answer important research questions.
    - Draw meaningful conclusions from the data.
    """)

    st.markdown("---")

    # Dataset Information
    st.header("📂 Dataset Information")

    st.write("""
    The dataset contains information about countries around the world, including:

    - 🌍 Country Name
    - 🌎 Continent
    - 👥 Population
    - 📍 Capital City
    - 📏 Area (km²)
    - 🏙 Population Density
    - 📈 Growth Rate
    - 🌐 World Population Percentage
    - 🏅 Rank
    """)

    st.markdown("---")

    # Technologies Used
    st.header("🛠 Technologies Used")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Programming Language
        - Python

        ### Libraries
        - Pandas
        - NumPy
        - Matplotlib
        """)

    with col2:
        st.markdown("""
        ### Visualization
        - Plotly Express
        - Streamlit

        ### Tools
        - Jupyter Notebook
        - VS Code
        - GitHub
        """)

    st.markdown("---")

    # Workflow
    st.header("⚙ Project Workflow")

    st.markdown("""
    1. Dataset Collection
    2. Data Cleaning
    3. Data Preprocessing
    4. Exploratory Data Analysis (EDA)
    5. Data Visualization
    6. Research Questions
    7. Conclusion
    """)

    st.markdown("---")

    # Features
    st.header("✨ Dashboard Features")

    st.success("""
    ✔ Home Page

    ✔ Dataset Overview

    ✔ Data Cleaning

    ✔ Exploratory Data Analysis (EDA)

    ✔ Research Questions

    ✔ Conclusion
    """)

    st.markdown("---")

    # Conclusion
    st.header("📖 Project Summary")

    st.write("""
    This dashboard provides a comprehensive analysis of the World Population
    dataset. Users can explore demographic information, visualize population
    trends, compare countries, and gain insights into global population
    statistics through interactive charts and tables.
    """)

    st.markdown("---")

    st.info("👉 Use the sidebar to navigate to Dataset, Data Cleaning, EDA, Research Questions, and Conclusion pages.")

    st.markdown("---")

    st.caption("Developed using ❤️ Python | Streamlit | Pandas | Plotly Express")
# =====================================
# DATASET PAGE
# =====================================
elif page == "Dataset":

    st.title("📂 World Population Dataset")

    st.markdown("### Dataset Overview")

    st.subheader("📄 Dataset")
    st.dataframe(df, use_container_width=True)

    st.subheader("📏 Dataset Shape")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.subheader("📝 Column Names")
    st.write(df.columns.tolist())

    st.subheader("🔍 Data Types")
    st.dataframe(df.dtypes.reset_index().rename(columns={"index":"Column",0:"Data Type"}))

    st.subheader("❗ Missing Values")
    st.dataframe(df.isnull().sum().reset_index().rename(columns={"index":"Column",0:"Missing Values"}))

    st.subheader("📊 Statistical Summary")
    st.dataframe(df.describe())

    st.subheader("🔝 First 5 Rows")
    st.dataframe(df.head())

    st.subheader("🔚 Last 5 Rows")
    st.dataframe(df.tail())

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Dataset",
        csv,
        "World_Population_Data.csv",
        "text/csv"
    )

# =====================================
# DATA CLEANING PAGE
# =====================================
elif page=="Data Cleaning":
    import matplotlib.pyplot as plt

    st.title("📊 Exploratory Data Analysis")

    # Top 10 Population Countries
    st.subheader("🌍 Top 10 Population Countries")

    top10 = df.sort_values("Population (2024)", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(top10["Country"], top10["Population (2024)"])
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Highest Density Countries
    st.subheader("🏙 Top 10 Highest Density Countries")

    density = df.sort_values("Density (per km²)", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(density["Country/Territory"], density["Density (per km²)"])
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Population Distribution
    st.subheader("📈 Population Distribution")

    fig, ax = plt.subplots(figsize=(8,5))
    ax.hist(df["2022 Population"], bins=20)
    st.pyplot(fig)
    # -------------------------------
# EDA PAGE
# -------------------------------
elif page == "📊 EDA":

    st.title("📊 Exploratory Data Analysis")

    # -------- Top 10 Population --------

    st.subheader("Top 10 Countries by Population")

    top10 = df.sort_values(
        by="Population",
        ascending=False
    ).head(10)

    fig1 = px.bar(
        top10,
        x="Country",
        y="Population",
        color="Population",
        title="Top 10 Population Countries"
    )

    st.plotly_chart(fig1, use_container_width=True)

    # -------- Population Distribution --------

    st.subheader("Population Distribution")

    fig2 = px.histogram(
        df,
        x="Population",
        nbins=30,
        title="Population Distribution"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # -------- Density --------

    if "Density (per km²)" in df.columns:

        st.subheader("Highest Density Countries")

        density = df.sort_values(
            by="Density (per km²)",
            ascending=False
        ).head(10)

        fig3 = px.bar(
            density,
            x="Country",
            y="Density (per km²)",
            color="Density (per km²)",
            title="Top 10 Highest Density Countries"
        )

        st.plotly_chart(fig3, use_container_width=True)

    # -------- Pie Chart --------

    st.subheader("Top 10 Population Share")

    fig4 = px.pie(
        top10,
        names="Country",
        values="Population",
        title="Top 10 Population Countries"
    )

    st.plotly_chart(fig4, use_container_width=True)

    # -------- Scatter --------

    if "Area (km²)" in df.columns:

        st.subheader("Population vs Area")

        fig5 = px.scatter(
            df,
            x="Area (km²)",
            y="Population",
            hover_name="Country",
            color="Population",
            title="Population vs Area"
        )

        st.plotly_chart(fig5, use_container_width=True)