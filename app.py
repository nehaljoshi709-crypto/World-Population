import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ---------------------------------------------------------
# Page Information & Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="World Population Analysis 2024",
    page_icon="🌍",
    layout="wide"
)

# ---------------------------------------------------------
# Project Title & Header
# ---------------------------------------------------------
st.title("🌍 World Population Analysis 2024")
st.markdown("---")

# ---------------------------------------------------------
# Sidebar & Navigation
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Select Section:",
    [
 "Home",
        "Dataset",
        "Data Cleaning",
        "EDA",
        "Research Questions",
        "Prediction Panel", 
        "Conclusion",
    ]
)
# ---------------------------------------------------------
# Home Page Section
# ---------------------------------------------------------
if page == "Home":
    st.subheader("👋 Welcome to the Dashboard!")
    st.markdown("---")

    # 📌 Project Description
    st.markdown("### 📖 Project Description")
    st.info(
        """
        This **World Population Analysis (2024)** project provides an interactive data analytics platform 
        to explore global demographic trends. It examines essential metrics such as country-wise population size, 
        density, growth rates, fertility rates, median age, and urban population percentages to deliver actionable 
        global insights.
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # 🎯 Project Objectives & 🌟 Key Features
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎯 Project Objectives")
        st.markdown(
            """
            * **Analyze Population Distribution:** Identify the most and least populated countries across the globe.
            * **Examine Density Trends:** Evaluate population density ($\text{P/km}^2$) across different land areas.
            * **Demographic Patterns:** Study the relationship between **Median Age** and **Fertility Rates**.
            * **Urbanization Insight:** Measure urban population growth and distribution across nations.
            * **Data-Driven Decision Making:** Provide clear, structured data views for researchers and analysts.
            """
        )

    with col2:
        st.markdown("### 🌟 Key Features")
        st.markdown(
            """
            * **Interactive Navigation:** Seamlessly switch between Dataset, Data Cleaning, EDA, and Insights.
            * **Real-time Data Filtering:** Dynamic controls to customize top/bottom country views.
            * **Rich Visualizations:** Interactive Plotly charts and Seaborn distributions.
            * **Data Cleaning Transparency:** View raw vs. cleaned dataset structure with missing value summaries.
            * **Key Takeaways & Insights:** Direct answers to core research questions.
            """
        )

    st.markdown("---")

    # 🛠️ Tools & Technologies Used
    st.markdown("### 🛠️ Tools & Technologies Used")
    
    t1, t2, t3, t4, t5 = st.columns(5)
    t1.metric("Frontend / App", "Streamlit")
    t2.metric("Data Processing", "Pandas")
    t3.metric("Numerical Computations", "NumPy")
    t4.metric("Interactive Plots", "Plotly")
    t5.metric("Static Plots", "Matplotlib / Seaborn")
# ---------------------------------------------------------
# Dataset Page Section (Fixed & Error-Free)
# ---------------------------------------------------------
elif page == "Dataset":
    st.title("📊 Dataset Overview & Information")
    st.markdown("---")

    # Safe Data Load Function with Cleaning
    @st.cache_data
    def load_data():
        df = pd.read_csv("World Population Data.csv")
        
        # Numeric conversion for Population column
        if 'Population (2024)' in df.columns and df['Population (2024)'].dtype == 'object':
            df['Population_Clean'] = df['Population (2024)'].astype(str).str.replace(',', '').str.strip()
            df['Population_Clean'] = pd.to_numeric(df['Population_Clean'], errors='coerce')
        else:
            df['Population_Clean'] = df['Population (2024)']
            
        return df

    try:
        df = load_data()

        # 📌 Top KPI Metrics
        st.subheader("📌 Key Dataset Metrics")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Records / Countries", f"{len(df)}")
        m2.metric("Total Columns", f"{df.shape[1] - 1}") # Excluding internal clean col
        m3.metric("Avg Fertility Rate", f"{df['Fert. Rate'].mean():.2f}")
        m4.metric("Avg Median Age", f"{df['Med. Age'].mean():.1f} Yrs")

        st.markdown("---")

        # 🔍 Interactive Raw Data Preview
        st.subheader("🔍 Dataset Preview")
        num_rows = st.slider("Select number of rows to view:", min_value=5, max_value=len(df), value=10, step=5)
        
        # Display original dataframe without temporary clean column
        display_cols = [col for col in df.columns if col != 'Population_Clean']
        st.dataframe(df[display_cols].head(num_rows), use_container_width=True)

        st.markdown("---")

        # 📋 Dataset Properties & Columns Info
        col_left, col_right = st.columns(2)

        with col_left:
            st.subheader("📋 Column Names & Data Types")
            info_df = pd.DataFrame({
                "Column Name": display_cols,
                "Data Type": df[display_cols].dtypes.astype(str),
                "Non-Null Count": df[display_cols].notnull().sum().values
            })
            st.dataframe(info_df, use_container_width=True)

        with col_right:
            st.subheader("📈 Summary Statistics")
            st.dataframe(df[display_cols].describe(), use_container_width=True)

    except Exception as e:
        st.error(f"⚠️ Error loading 'World Population Data.csv': {e}")
        st.info("Please make sure 'World Population Data.csv' is saved in the same directory as this app.py file.")
        import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# Data Cleaning & Exploration Page Section
# ---------------------------------------------------------
if page == "Data Cleaning":
    st.title("🧹 Data Cleaning & Preprocessing")
    st.markdown("In this page checks, missing values, duplicates, outliers ,first five rows,last five rows,shape of dadtaset")
    st.markdown("---")

    @st.cache_data
    def load_data():
        return pd.read_csv("World Population Data.csv")

    try:
        df = load_data()

        # ---------------------------------------------------------
        # 1. Dataset Shape & Summary Overview
        # ---------------------------------------------------------
        st.subheader("📌 1. Dataset Shape & Quick Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        col1.metric("Total Rows (Entries)", f"{df.shape[0]}")
        col2.metric("Total Columns", f"{df.shape[1]}")
        col3.metric("Missing/Null Values", f"{df.isnull().sum().sum()}")
        col4.metric("Duplicate Rows", f"{df.duplicated().sum()}")

        st.markdown("---")

        # ---------------------------------------------------------
        # 2. Head & Tail View
        # ---------------------------------------------------------
        st.subheader("👀 2. Data Preview (Head & Tail)")
        tab_head, tab_tail = st.tabs(["🔝 First Rows (Head)", "🔻 Last Rows (Tail)"])
        
        with tab_head:
            n_head = st.slider("Select rows for Head:", 3, 20, 5, key="head_slider")
            st.dataframe(df.head(n_head), use_container_width=True)
            
        with tab_tail:
            n_tail = st.slider("Select rows for Tail:", 3, 20, 5, key="tail_slider")
            st.dataframe(df.tail(n_tail), use_container_width=True)

        st.markdown("---")

        # ---------------------------------------------------------
        # 3. Data Info, Missing Values & Unique Values
        # ---------------------------------------------------------
        st.subheader("🔍 3. Data Info, Missing & Unique Values")
        
        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("### 📋 Column-wise Analysis Table")
            summary_info = pd.DataFrame({
                "Data Type": df.dtypes.astype(str),
                "Null Values": df.isnull().sum(),
                "Null %": (df.isnull().sum() / len(df) * 100).round(2).astype(str) + "%",
                "Unique Values": df.nunique()
            })
            st.dataframe(summary_info, use_container_width=True)

        with col_right:
            st.markdown("### 🧬 Duplicates & Data Health Check")
            st.success(f"✅ **Duplicate Records:** {df.duplicated().sum()} rows found.")
            if df.isnull().sum().sum() == 0:
                st.success("✅ **Missing Values:** there is no missing values in dataset.")
            else:
                st.warning(f"⚠️ **Missing Values:** Total {df.isnull().sum().sum()} missing values paaye gaye hain.")

            st.info("""
            **Summary Observations:**
            * Dataset is already clean no missing values.
            * There are no duplicated value in dataset.
            * Columns  'Population (2024)', 'Density' are in the string format than the EDA convert the numeric values.  
            """)

        st.markdown("---")

        # ---------------------------------------------------------
        # 4. Outliers Detection
        # ---------------------------------------------------------
        st.subheader("⚠️ 4. Outliers Analysis")
        st.markdown("---")

        # Filter numeric columns for Boxplot
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

        if numeric_cols:
            selected_col = st.selectbox("Select Numerical Feature for Outlier Detection:", numeric_cols)

            col_box, col_stats = st.columns([2, 1])

            with col_box:
                fig_box = px.box(
                    df, 
                    y=selected_col, 
                    points="all", 
                    title=f"Boxplot for '{selected_col}'",
                    color_discrete_sequence=['#E74C3C']
                )
                st.plotly_chart(fig_box, use_container_width=True)

            with col_stats:
                st.markdown(f"### 📊 Stats for `{selected_col}`")
                q1 = df[selected_col].quantile(0.25)
                q3 = df[selected_col].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                
                outliers_count = df[(df[selected_col] < lower_bound) | (df[selected_col] > upper_bound)].shape[0]

                st.write(f"**Q1 (25th Percentile):** {q1:.2f}")
                st.write(f"**Q3 (75th Percentile):** {q3:.2f}")
                st.write(f"**IQR:** {iqr:.2f}")
                st.write(f"**Upper Bound:** {upper_bound:.2f}")
                st.write(f"**Lower Bound:** {lower_bound:.2f}")
                st.metric("Detected Outliers", f"{outliers_count}")

    except Exception as e:
        st.error(f"⚠️ Error loading data: {e}")
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# EDA Page Section (With Requested Specific Chart Types)
# ---------------------------------------------------------
if page == "EDA":
    st.title("📈 Exploratory Data Analysis (EDA)")
    st.markdown("---")

    # Preprocessing Function
    @st.cache_data
    def load_and_prep_eda_data():
        df = pd.read_csv("World Population Data.csv")
        
        # Clean numeric columns safely
        def clean_col(col_name):
            return pd.to_numeric(
                df[col_name].astype(str)
                .str.replace(',', '', regex=False)
                .str.replace('%', '', regex=False)
                .str.replace('N.A.', '0', regex=False)
                .str.strip(), 
                errors='coerce'
            )

        df['Pop_Clean'] = clean_col('Population (2024)')
        df['Density_Clean'] = clean_col('Density (P/Km²)')
        df['Yearly_Change_Clean'] = clean_col('Yearly Change')
        df['Net_Change_Clean'] = clean_col('Net Change')
        df['Land_Area_Clean'] = clean_col('Land Area (Km²)')
        df['Migrants_Clean'] = clean_col('Migrants (net)')
        df['Urban_Pop_Clean'] = clean_col('Urban Pop %')
        df['World_Share_Clean'] = clean_col('World Share')

        return df

    try:
        df_eda = load_and_prep_eda_data()

        # Dynamic Slider in Sidebar
        top_n = st.sidebar.slider("Select Top Count (N):", min_value=5, max_value=20, value=10)

        # =========================================================
        # 1. BAR CHART: Top N Most Populated Countries
        # =========================================================
        st.subheader(f"1. 📊 Bar Chart: Top {top_n} Most Populated Countries")
        top_pop = df_eda.sort_values(by="Pop_Clean", ascending=False).head(top_n)
        
        fig1 = px.bar(
            top_pop,
            x="Country",
            y="Pop_Clean",
            text="Pop_Clean",
            color="Pop_Clean",
            color_continuous_scale="Blues",
            labels={"Pop_Clean": "Population (2024)", "Country": "Country"}
        )
        fig1.update_traces(texttemplate='%{text:.3s}', textposition='outside')
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("---")

        # =========================================================
        # 2. PIE CHART: World Share Distribution
        # =========================================================
        st.subheader(f"2. 🍕 Pie Chart: World Population Share (Top {top_n} vs Others)")
        
        top_share = top_pop.copy()
        other_share_val = 100 - top_share['World_Share_Clean'].sum()
        other_row = pd.DataFrame([{'Country': 'Rest of the World', 'World_Share_Clean': other_share_val}])
        pie_df = pd.concat([top_share[['Country', 'World_Share_Clean']], other_row], ignore_index=True)

        fig2 = px.pie(
            pie_df,
            names="Country",
            values="World_Share_Clean",
            title=f"Top {top_n} Countries vs Rest of the World (% Share)",
            hole=0.3,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("---")

        # =========================================================
        # 3. SCATTER PLOT: Median Age vs Fertility Rate
        # =========================================================
        st.subheader("3. 🔴 Scatter Plot: Median Age vs. Fertility Rate")

        fig3 = px.scatter(
            df_eda,
            x="Med. Age",
            y="Fert. Rate",
            size="Pop_Clean",
            color="Yearly_Change_Clean",
            hover_name="Country",
            labels={
                "Med. Age": "Median Age (Years)", 
                "Fert. Rate": "Fertility Rate", 
                "Yearly_Change_Clean": "Yearly Growth (%)"
            },
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("---")

        # =========================================================
        # 4. LINE CHART: Top Densest Countries
        # =========================================================
        st.subheader(f"4. 📈 Line Chart: Population Density Trend (Top {top_n} Dense)")
        top_dense = df_eda.sort_values(by="Density_Clean", ascending=False).head(top_n)

        fig4 = px.line(
            top_dense,
            x="Country",
            y="Density_Clean",
            markers=True,
            title=f"Population Density Comparison (Top {top_n} Countries)",
            labels={"Density_Clean": "Density (P/Km²)"}
        )
        fig4.update_traces(line_color='#E74C3C', line_width=3, marker_size=10)
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown("---")

        # =========================================================
        # 5. 3D GRAPH: 3D Scatter Plot (Land Area vs Density vs Population)
        # =========================================================
        st.subheader("5. 🧊 3D Graph: Land Area vs Density vs Population")

        fig5 = px.scatter_3d(
            df_eda,
            x="Land_Area_Clean",
            y="Density_Clean",
            z="Pop_Clean",
            color="Yearly_Change_Clean",
            hover_name="Country",
            size="Pop_Clean",
            size_max=30,
            labels={
                "Land_Area_Clean": "Land Area (Km²)",
                "Density_Clean": "Density (P/Km²)",
                "Pop_Clean": "Population"
            },
            color_continuous_scale="Turbo"
        )
        fig5.update_layout(height=600)
        st.plotly_chart(fig5, use_container_width=True)

        st.markdown("---")

        # =========================================================
        # 6. HISTOGRAM: Urban Population (%) Distribution
        # =========================================================
        st.subheader("6. 📊 Histogram: Urban Population (%) Distribution")

        fig6 = px.histogram(
            df_eda,
            x="Urban_Pop_Clean",
            nbins=20,
            color_discrete_sequence=['#2ECC71'],
            labels={"Urban_Pop_Clean": "Urban Population (%)"},
            title="Frequency Distribution of Urbanization Rate Across World"
        )
        st.plotly_chart(fig6, use_container_width=True)
        st.markdown("---")

        # =========================================================
        # 7. BOX PLOT: Yearly Change % Outliers & Spread
        # =========================================================
        st.subheader("7. 📦 Box Plot: Growth Rate (%) Spread & Outliers")

        fig7 = px.box(
            df_eda,
            y="Yearly_Change_Clean",
            points="all",
            hover_name="Country",
            title="Distribution and Outliers in Yearly Growth Rate (%)",
            labels={"Yearly_Change_Clean": "Yearly Change (%)"},
            color_discrete_sequence=['#9B59B6']
        )
        st.plotly_chart(fig7, use_container_width=True)
        st.markdown("---")

        # =========================================================
        # 8. DIVERGING BAR CHART: Migration Inflow vs Outflow
        # =========================================================
        st.subheader(f"8. 🔄 Net Migration (Inflow vs Outflow)")

        top_migrants = df_eda.sort_values(by="Migrants_Clean", ascending=False).head(5)
        bottom_migrants = df_eda.sort_values(by="Migrants_Clean", ascending=True).head(5)
        mig_df = pd.concat([top_migrants, bottom_migrants])

        fig8 = px.bar(
            mig_df,
            x="Country",
            y="Migrants_Clean",
            color="Migrants_Clean",
            color_continuous_scale="RdBu",
            labels={"Migrants_Clean": "Net Migrants"},
            title="Top 5 Countries with Positive vs Negative Net Migration"
        )
        st.plotly_chart(fig8, use_container_width=True)

    except Exception as e:
        st.error(f"⚠️ Error rendering EDA charts: {e}")
        import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------------
# Research Questions Page Section
# ---------------------------------------------------------
if page == "Research Questions":
    st.title("❓ Key Research Questions & Analysis")
    st.markdown("---")

    # Data Preprocessing Function
    @st.cache_data
    def load_prep_rq_data():
        df = pd.read_csv("World Population Data.csv")
        
        def clean_col(col_name):
            return pd.to_numeric(
                df[col_name].astype(str)
                .str.replace(',', '', regex=False)
                .str.replace('%', '', regex=False)
                .str.replace('N.A.', '0', regex=False)
                .str.strip(), 
                errors='coerce'
            )

        df['Pop_Clean'] = clean_col('Population (2024)')
        df['Density_Clean'] = clean_col('Density (P/Km²)')
        df['Yearly_Change_Clean'] = clean_col('Yearly Change')
        df['Land_Area_Clean'] = clean_col('Land Area (Km²)')
        df['Migrants_Clean'] = clean_col('Migrants (net)')
        df['Urban_Pop_Clean'] = clean_col('Urban Pop %')
        df['World_Share_Clean'] = clean_col('World Share')

        return df

    try:
        df_rq = load_prep_rq_data()

        # =========================================================
        # RESEARCH QUESTION 1
        # =========================================================
        st.subheader("Q1: Which countries drive the majority of global population growth?")
        
        top_growth_net = df_rq.sort_values(by="Net Change", ascending=False).head(10)

        fig_q1 = px.bar(
            top_growth_net,
            x="Country",
            y="Net Change",
            text="Net Change",
            color="Net Change",
            color_continuous_scale="Teal",
            labels={"Net Change": "Annual Net Population Increase"},
            title="Top 10 Countries by Highest Annual Net Population Increase"
        )
        fig_q1.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        st.plotly_chart(fig_q1, use_container_width=True)

        st.success("""
        📌 **Insights:**
        * **India** sabse zyada annual net population addition (~12.8M per year) register kar raha hai, uske baad **Pakistan** (~3.7M) aur **Nigeria** (~3.2M) hain.
        * **China** high population waala desh hone ke bawajood negative population growth (-3.2M net change) show kar raha hai.
        """)
        st.markdown("---")

        # =========================================================
        # RESEARCH QUESTION 2
        # =========================================================
        st.subheader("Q2: Is there a significant relationship between Urbanization (%) and Fertility Rate?")

        fig_q2 = px.scatter(
            df_rq,
            x="Urban_Pop_Clean",
            y="Fert. Rate",
            color="Med. Age",
            hover_name="Country",
            labels={
                "Urban_Pop_Clean": "Urban Population (%)",
                "Fert. Rate": "Fertility Rate (Children per Woman)",
                "Med. Age": "Median Age"
            },
            title="Urbanization (%) vs Fertility Rate with Trendline",
            color_continuous_scale="Viridis"
        )
        st.plotly_chart(fig_q2, use_container_width=True)

        st.success("""
        📌 **Insights:**
        * **Negative Trend:** High Urbanization rate wale deshon me Fertility Rate kaafi low hai.
        * **Economic Impact:** Urban lifestyle, better education, aur high living costs family size chhota rakhne me contribute karte hain.
        """)
        st.markdown("---")

        # =========================================================
        # RESEARCH QUESTION 3
        # =========================================================
        st.subheader("Q3: How does Population Density compare across different Land Area scales?")

        fig_q3 = px.scatter(
            df_rq,
            x="Land_Area_Clean",
            y="Density_Clean",
            size="Pop_Clean",
            color="Urban_Pop_Clean",
            hover_name="Country",
            log_x=True,
            log_y=True,
            labels={
                "Land_Area_Clean": "Land Area (Km² - Log Scale)",
                "Density_Clean": "Density (P/Km² - Log Scale)",
                "Urban_Pop_Clean": "Urban Pop (%)"
            },
            title="Land Area vs Population Density (Logarithmic Scale)",
            color_continuous_scale="Plasma"
        )
        st.plotly_chart(fig_q3, use_container_width=True)

        st.success("""
        📌 **Insights:**
        * Log scale analysis dikhata hai ki sabse high density microstates (jaise Monaco, Macao, Singapore) me land area minimum hai.
        * Bade deshon (jaise Russia, Canada, Australia) me total land area bahut bada hone ki wajah se average density kaafi kam rehti hai.
        """)
        st.markdown("---")

        # =========================================================
        # RESEARCH QUESTION 4
        # =========================================================
        st.subheader("Q4: What is the impact of Net Migration on highly developed vs developing nations?")

        # Top 5 Inflow & Top 5 Outflow
        top_inflow = df_rq.sort_values(by="Migrants_Clean", ascending=False).head(5)
        top_outflow = df_rq.sort_values(by="Migrants_Clean", ascending=True).head(5)
        mig_q4 = pd.concat([top_inflow, top_outflow])

        fig_q4 = px.bar(
            mig_q4,
            x="Country",
            y="Migrants_Clean",
            color="Migrants_Clean",
            color_continuous_scale="RdYlGn",
            labels={"Migrants_Clean": "Net Migration Value"},
            title="Top Net Inflow (Immigration) vs Net Outflow (Emigration) Countries"
        )
        st.plotly_chart(fig_q4, use_container_width=True)

        st.success("""
        📌 **Insights:**
        * **Highest Net Inflow:** USA (~1.28M) aur Germany me sabse zyada positive net migration hai, jo economic job opportunities ko highlight karta hai.
        * **Highest Net Outflow:** Pakistan (-1.4M) aur India (-630K) me highest net outflow dekha gaya hai due to labor and workforce migration.
        """)
        st.markdown("---")

        # =========================================================
        # RESEARCH QUESTION 5
        # =========================================================
        st.subheader("Q5: What is the global aging scenario based on Median Age distribution?")

        # Categorize Median Age into Age Groups
        def age_group(age):
            if age < 20:
                return "Very Young (<20 yrs)"
            elif age <= 35:
                return "Youth / Working (20-35 yrs)"
            elif age <= 45:
                return "Mature (36-45 yrs)"
            else:
                return "Aging (>45 yrs)"

        df_rq['Age_Group'] = df_rq['Med. Age'].apply(age_group)

        fig_q5 = px.pie(
            df_rq,
            names="Age_Group",
            values="Pop_Clean",
            title="Global Population Distribution by Median Age Categories",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig_q5, use_container_width=True)

        st.success("""
        📌 **Insights:**
        * Global population ka sabse bada share **Youth / Working Class (20-35 years)** category me aata hai.
        * Developing nations (Africa/South Asia) young demographic dividend hold karte hain, jabki Developed nations aging population challenge face kar rahe hain.
        """)

    except Exception as e:
        st.error(f"⚠️ Error rendering Research Questions: {e}")
        # Interactive Prediction Panel Page Section
# ---------------------------------------------------------
elif page == "Prediction Panel":
    st.title("🔮 Interactive Future Population Predictor")
    st.markdown(
        "Simulate future population projections using empirical demographic features and adjustable custom compound trends."
    )
    st.markdown("---")

    # Safe Internal Processing & Data Loading
    @st.cache_data
    def load_clean_prediction_data():
        df = pd.read_csv("World Population Data.csv")

        def clean_col(col_name):
            return pd.to_numeric(
                df[col_name]
                .astype(str)
                .str.replace(",", "", regex=False)
                .str.replace("%", "", regex=False)
                .str.replace("N.A.", "0", regex=False)
                .str.strip(),
                errors="coerce",
            )

        df["Pop_Clean"] = clean_col("Population (2024)")
        df["Yearly_Change_Clean"] = clean_col("Yearly Change")
        df["Net_Change_Clean"] = clean_col("Net Change")
        df["Land_Area_Clean"] = clean_col("Land Area (Km²)")
        df["Density_Clean"] = clean_col("Density (P/Km²)")
        df["Fert_Rate_Clean"] = clean_col("Fert. Rate")
        df["Med_Age_Clean"] = clean_col("Med. Age")

        # Fallback values fill for missing fields
        df["Fert_Rate_Clean"] = df["Fert_Rate_Clean"].fillna(
            df["Fert_Rate_Clean"].median()
        )
        df["Med_Age_Clean"] = df["Med_Age_Clean"].fillna(
            df["Med_Age_Clean"].median()
        )

        return df

    try:
        df_pred = load_clean_prediction_data()

        # Split UI into Two Pillars: Left for Selectors, Right for Dynamic Forecast Outputs
        col_controls, col_display = st.columns([1, 2])

        with col_controls:
            st.subheader("🛠️ Simulation Controls")

            # Country Selector Dropdown Array
            target_country = st.selectbox(
                "Choose Country to Profile:", df_pred["Country"].unique()
            )

            # Extract Baseline Metrics of selected country
            row = df_pred[df_pred["Country"] == target_country].iloc[0]
            base_pop = int(row["Pop_Clean"])
            base_growth = float(row["Yearly_Change_Clean"])
            base_fertility = float(row["Fert_Rate_Clean"])
            base_age = float(row["Med_Age_Clean"])
            base_area = float(row["Land_Area_Clean"])

            st.markdown("### 🎛️ Adjust Scenario Multipliers")

            # Timeline Horizon Slider
            target_years = st.slider(
                "Prediction Horizon (Years from 2024):",
                min_value=1,
                max_value=50,
                value=15,
                step=1,
            )

            # Growth Factor Interactive Slider
            custom_growth = st.slider(
                "Simulated Yearly Growth Rate (%):",
                min_value=-3.0,
                max_value=6.0,
                value=base_growth,
                step=0.05,
            )

            # Secondary Analytics Toggles
            st.caption("Hypothetical Impact Parameters")
            fertility_shift = st.slider(
                "Custom Fertility Rate Shift:",
                min_value=0.5,
                max_value=7.0,
                value=base_fertility,
                step=0.1,
            )

        with col_display:
            st.subheader(f"📊 Forecasting Matrix for {target_country}")

            # Calculation Step using CAGR Equation: P_future = P_current * (1 + r)^t
            simulated_rate = custom_growth / 100.0
            predicted_population = int(base_pop * ((1 + simulated_rate) ** target_years))
            population_delta = predicted_population - base_pop
            target_future_year = 2024 + target_years

            # New Density Calculation
            predicted_density = (
                predicted_population / base_area if base_area > 0 else 0
            )

            # Display KPI Result Blocks
            kpi1, kpi2, kpi3 = st.columns(3)
            kpi1.metric(
                label=f"Projected Population ({target_future_year})",
                value=f"{predicted_population:,}",
            )
            kpi2.metric(
                label="Net Simulation Shift",
                value=f"{population_delta:+,}",
                delta=f"{custom_growth - base_growth:+.2f}% vs Baseline",
            )
            kpi3.metric(
                label="Projected Density",
                value=f"{predicted_density:,.1f} P/Km²",
            )

            st.markdown("---")

            # Time Series Progression Plot Generation
            st.markdown(f"#### 📈 Year-on-Year Trend Projection to {target_future_year}")

            years_arr = np.arange(2024, target_future_year + 1)
            pop_trend = [
                int(base_pop * ((1 + simulated_rate) ** (y - 2024))) for y in years_arr
            ]

            trend_data = pd.DataFrame(
                {"Year": years_arr, "Estimated Population": pop_trend}
            )

            fig_trend = px.line(
                trend_data,
                x="Year",
                y="Estimated Population",
                markers=True,
                title=f"Growth Path Vector for {target_country}",
                labels={"Estimated Population": "Population Bounds"},
            )
            fig_trend.update_traces(line_color="#2ECC71", line_width=3)
            st.plotly_chart(fig_trend, use_container_width=True)

            # Informative Validation Insight Notes Based on Inputs
            st.info(
                f"""
            💡 **Simulation Analysis Summary:**
            * Baseline Population in 2024 for **{target_country}** is **{base_pop:,}** with a default growth vector of **{base_growth}%**.
            * Modifying the rate dynamically to **{custom_growth}%** produces a forecasted configuration shift of **{population_delta:,}** citizens over a span of **{target_years} years**.
            * The spatial pressure index adjustments will update the area density limits to **{predicted_density:,.1f} occupants per square kilometer** across a fixed land boundaries grid of **{base_area:,} Km²**.
            """
            )

    except Exception as prediction_error:
        st.error(f"❌ Failed to execute system simulations: {prediction_error}")
        st.info(
            "Verify that 'World Population Data.csv' is properly cleaned and present inside the execution directory."
        )
        # ---------------------------------------------------------
# Conclusion & Summary Page Section
# ---------------------------------------------------------
elif page == "Conclusion":
    st.title("📌 Project Conclusion & Executive Summary")
    st.markdown("---")

    # 🎯 Executive Summary Banner
    st.subheader("🎯 Executive Summary")
    st.success(
        """
        **World Population Analysis (2024)** dashboard highlights major demographic shifts, 
        regional imbalances, and structural population dynamics. The insights gathered from this study 
        are crucial for policymakers, urban planners, and economic analysts to prepare for future resource distribution.
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # 📊 Major Findings & Takeaways
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔍 Key Analytical Findings")
        st.markdown(
            """
            * **Population Concentration:** The majority of the global population remains heavily concentrated in **Asia** (led by India and China), accounting for over 50% of total world share.
            * **Fertility & Urbanization Inversion:** Higher urbanization strongly correlates with declining fertility rates, creating future demographic shrinkages in highly urbanized nations.
            * **The Demographic Dividend:** Developing regions (especially sub-Saharan Africa and parts of South Asia) hold the highest youth population percentage (Median Age < 20).
            * **Migration Trends:** Economic hubs like the **USA** and **Germany** continue to pull net positive migration, whereas countries experiencing economic instability show strong net emigration.
            """
        )

    with col2:
        st.markdown("### 💡 Policy & Future Implications")
        st.markdown(
            """
            * **Resource Management:** Nations with rapidly growing populations must focus on sustainable infrastructure, healthcare, and water supply.
            * **Aging Population Challenge:** Developed nations with high median ages (>40 yrs) will face labor shortages and increased pension/healthcare burdens.
            * **Urban Planning:** Accelerated urban shift requires modern smart-city planning and affordable housing initiatives.
            * **Skill Migration & Brain Drain:** Outflow countries need policy incentives to retain skilled talent locally.
            """
        )

    st.markdown("---")

    # 🛠️ Technical Wrap-up & Project Deliverables Summary
    st.subheader("🛠️ Technical Project Deliverables")
    
    t1, t2, t3, t4 = st.columns(4)
    t1.metric("Data Cleaning", "100% Non-Null")
    t2.metric("Total Visualizations", "12+ Charts")
    t3.metric("Research Questions", "5 Core Insights")
    t4.metric("UI Responsiveness", "Streamlit Native")

    st.markdown("<br>", unsafe_allow_html=True)

    # 🤝 Thank You Note
    st.info("🎉 **Thank you for exploring the World Population Analysis Dashboard!**")