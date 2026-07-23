import streamlit as st

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="World Population Analysis",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------
# Custom CSS
# ---------------------------------
st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

.title{
    font-size:48px;
    font-weight:bold;
    text-align:center;
    color:white;
}

.subtitle{
    font-size:22px;
    text-align:center;
    color:white;
}

.header{
    background:linear-gradient(90deg,#1565C0,#42A5F5,#26C6DA);
    padding:35px;
    border-radius:18px;
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    box-shadow:0px 3px 12px rgba(0,0,0,0.12);
}

.feature{
    background:#ffffff;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.1);
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Sidebar
# ---------------------------------

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/616/616494.png",
    width=120
)

st.sidebar.title("🌍 Navigation")

st.sidebar.success("Select a page from the sidebar.")

st.sidebar.markdown("---")

st.sidebar.info("""
### Project Sections

🏠 Home

📂 Dataset

🧹 Data Cleaning

📊 EDA

📈 Visualizations

❓ Research Questions

📝 Conclusion
""")

# ---------------------------------
# Header
# ---------------------------------

st.markdown("""
<div class="header">

<div class="title">
🌍 World Population Analysis Dashboard
</div>

<div class="subtitle">
Interactive Data Analytics using Python, Pandas, Plotly & Streamlit
</div>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------------------------
# KPI Cards
# ---------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Dataset",
        "World Population"
    )

with c2:
    st.metric(
        "Countries",
        "230+"
    )

with c3:
    st.metric(
        "Technology",
        "Streamlit"
    )

with c4:
    st.metric(
        "Visualizations",
        "Interactive"
    )

st.write("")

# ---------------------------------
# About Project
# ---------------------------------

left,right = st.columns([2,1])

with left:

    st.markdown("""
<div class="card">

## 📖 About the Project

This project provides an in-depth analysis of the **World Population Dataset** using modern data analytics techniques.

The dashboard helps users understand:

- 🌍 Global population distribution
- 📈 Population growth trends
- 🌎 Country-wise comparison
- 🏙 Population density analysis
- 📊 Interactive visualizations
- 📉 Statistical insights

The application is fully interactive and allows users to explore population data efficiently.

</div>
""",unsafe_allow_html=True)

with right:

    st.info("""
### 🎯 Project Objectives

✔ Analyze world population

✔ Compare countries

✔ Study population density

✔ Understand growth trends

✔ Build an interactive dashboard

✔ Generate useful insights
""")

st.write("")

# ---------------------------------
# Features
# ---------------------------------

st.subheader("🚀 Project Features")

a,b,c = st.columns(3)

with a:
    st.markdown("""
<div class="feature">

## 📂

### Dataset

Clean and explore the dataset with detailed statistics.

</div>
""",unsafe_allow_html=True)

with b:
    st.markdown("""
<div class="feature">

## 🧹

### Data Cleaning

Handle missing values, duplicates, outliers and datatypes.

</div>
""",unsafe_allow_html=True)

with c:
    st.markdown("""
<div class="feature">

## 📊

### EDA

Interactive charts and statistical analysis.

</div>
""",unsafe_allow_html=True)

st.write("")

d,e,f = st.columns(3)

with d:
    st.markdown("""
<div class="feature">

## 📈

### Visualizations

Beautiful Plotly charts with filters.

</div>
""",unsafe_allow_html=True)

with e:
    st.markdown("""
<div class="feature">

## ❓

### Research Questions

Answer important population-related questions.

</div>
""",unsafe_allow_html=True)

with f:
    st.markdown("""
<div class="feature">

## 📝

### Conclusion

Summarize findings and insights.

</div>
""",unsafe_allow_html=True)

st.write("")

# ---------------------------------
# Technology Used
# ---------------------------------

st.subheader("💻 Technologies Used")

t1,t2,t3,t4,t5 = st.columns(5)

t1.success("Python")
t2.success("Pandas")
t3.success("NumPy")
t4.success("Plotly")
t5.success("Streamlit")

st.write("")

# ---------------------------------
# Workflow
# ---------------------------------

st.subheader("📌 Project Workflow")

st.markdown("""
1️⃣ Load Dataset

⬇

2️⃣ Data Cleaning

⬇

3️⃣ Exploratory Data Analysis

⬇

4️⃣ Interactive Visualizations

⬇

5️⃣ Research Questions

⬇

6️⃣ Insights & Conclusion
""")

st.write("")

# ---------------------------------
# Motivation
# ---------------------------------

st.subheader("🌎 Why World Population Analysis?")

st.write("""

Understanding population trends is essential for:

- Government planning
- Urban development
- Resource allocation
- Healthcare management
- Education planning
- Economic forecasting
- Sustainable development

""")

st.write("")

# ---------------------------------
# Footer
# ---------------------------------

st.markdown("---")

st.markdown("""
<div class="footer">

### 🌍 World Population Analysis Dashboard

Developed using ❤️ Python | Pandas | Plotly | Streamlit

</div>
""",unsafe_allow_html=True)
import streamlit as st
import pandas as pd

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Dataset",
    page_icon="📂",
    layout="wide"
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("World Population Data(5).csv")

df = load_data()

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.title("📂 Dataset Explorer")
st.markdown("Explore the World Population dataset interactively.")

st.markdown("---")

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------
c1, c2, c3, c4 = st.columns(4)

c1.metric("📄 Rows", f"{df.shape[0]:,}")
c2.metric("📑 Columns", df.shape[1])
c3.metric("❌ Missing Values", int(df.isnull().sum().sum()))
c4.metric("♻ Duplicate Rows", int(df.duplicated().sum()))

st.markdown("---")

# ---------------------------------------------------
# Dataset Preview
# ---------------------------------------------------
st.subheader("📋 Dataset Preview")

rows = st.slider(
    "Number of Rows",
    min_value=5,
    max_value=min(100, len(df)),
    value=10
)

st.dataframe(df.head(rows), use_container_width=True)

# ---------------------------------------------------
# Search
# ---------------------------------------------------
st.subheader("🔍 Search Dataset")

search = st.text_input("Search by Country")

if search:
    if "Country" in df.columns:
        result = df[df["Country"].astype(str).str.contains(search, case=False)]
        st.dataframe(result, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# Filter
# ---------------------------------------------------
if "Continent" in df.columns:

    st.subheader("🌍 Filter by Continent")

    continent = st.selectbox(
        "Choose Continent",
        ["All"] + sorted(df["Continent"].dropna().unique().tolist())
    )

    if continent != "All":
        filtered = df[df["Continent"] == continent]
        st.dataframe(filtered, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# Dataset Information
# ---------------------------------------------------
st.subheader("📊 Dataset Information")

info = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str),
    "Missing Values": df.isnull().sum().values,
    "Unique Values": df.nunique().values
})

st.dataframe(info, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# Numerical Summary
# ---------------------------------------------------
st.subheader("📈 Statistical Summary")

st.dataframe(df.describe(), use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# Missing Values
# ---------------------------------------------------
st.subheader("❌ Missing Values")

missing = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum(),
    "Percentage": (df.isnull().sum()/len(df)*100).round(2)
})

st.dataframe(missing, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# Duplicate Records
# ---------------------------------------------------
st.subheader("♻ Duplicate Records")

duplicates = df[df.duplicated()]

if len(duplicates) == 0:
    st.success("✅ No Duplicate Records Found")
else:
    st.warning(f"{len(duplicates)} Duplicate Rows Found")
    st.dataframe(duplicates, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------
# Column Selector
# ---------------------------------------------------
st.subheader("📌 Explore Individual Columns")

column = st.selectbox(
    "Select a Column",
    df.columns
)

st.write("### Data Type")
st.info(df[column].dtype)

st.write("### Unique Values")
st.write(df[column].nunique())

st.write("### Sample Values")
st.write(df[column].head(20))

st.markdown("---")

# ---------------------------------------------------
# Download Dataset
# ---------------------------------------------------
st.subheader("📥 Download Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Dataset",
    data=csv,
    file_name="World_Population_Data.csv",
    mime="text/csv"
)

st.markdown("---")

st.success("✅ Dataset exploration completed successfully.")