
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

st.set_page_config(page_title="⚡ Prediksi Permintaan Listrik", layout="wide")

# ============ Load Data ============ #
@st.cache_data
def load_data():
    return pd.read_csv('historic_demand_2000 (1).csv')

df = load_data()

features = [
    'embedded_wind_generation', 'embedded_solar_generation', 'scottish_transfer',
    'ifa_flow', 'ifa2_flow', 'britned_flow', 'moyle_flow', 'east_west_flow',
    'nemo_flow', 'nsl_flow', 'eleclink_flow', 'viking_flow', 'greenlink_flow'
]
target = 'england_wales_demand'

# ============ Modular Sections ============ #
def show_eda(df):
    st.header("📊 A. EDA dan Visualisasi Data")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔍 Tinjauan Data")
        st.dataframe(df.head())
    with col2:
        st.subheader("📈 Distribusi Permintaan Listrik")
        fig1 = px.histogram(df, x=target, nbins=30, title="Distribusi Demand", color_discrete_sequence=['#1f77b4'])
        st.plotly_chart(fig1, use_container_width=True)

    st.subheader("🌤️ Embedded Wind vs Solar Generation")
    fig2 = px.scatter(df, x='embedded_wind_generation', y='embedded_solar_generation',
                      title="Wind vs Solar Generation", color_discrete_sequence=['#2ca02c'])
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🔋 Rata-rata Produksi vs Permintaan")
    avg_data = {
        'Embedded Wind': df['embedded_wind_generation'].mean(),
        'Embedded Solar': df['embedded_solar_generation'].mean(),
        'Demand': df[target].mean()
    }
    avg_df = pd.DataFrame(avg_data.items(), columns=['Sumber', 'Rata-rata (MW)'])
    fig_bar = px.bar(avg_df, x='Sumber', y='Rata-rata (MW)', color='Sumber',
                     title='Rata-rata Output vs Permintaan', color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig_bar, use_container_width=True)

def show_correlation(df):
    st.header("🔗 B. Analisis Korelasi")
    st.subheader("🧭 Korelasi Interaktif")
    corr = df[features + [target]].corr().round(2)
    fig_corr_plotly = ff.create_annotated_heatmap(
        z=corr.values, x=list(corr.columns), y=list(corr.index),
        annotation_text=corr.values, colorscale='Viridis', showscale=True
    )
    st.plotly_chart(fig_corr_plotly, use_container_width=True)

    st.subheader("📊 Korelasi Statistik")
    fig_corr, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig_corr)

def train_model(df):
    st.header("🧠 C. Model Regresi Linier & Evaluasi")

    X = df[features]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression().fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.success("✅ Model berhasil dilatih!")

    st.subheader("📏 D. Evaluasi Model")
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.markdown(f"- **MAE:** `{mae:.2f}`")
    st.markdown(f"- **RMSE:** `{rmse:.2f}`")
    st.markdown(f"- **MSE:** `{mse:.2f}`")
    st.markdown(f"- **R-squared (R²):** `{r2:.4f}`")

    st.subheader("📊 Prediksi vs Aktual (100 Data Pertama)")
    chart_df = pd.DataFrame({"Aktual": y_test.values[:100], "Prediksi": y_pred[:100]})
    fig3 = px.line(chart_df, title="Aktual vs Prediksi", labels={"value": "Demand (MW)", "index": "Index"})
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("🔢 Koefisien Regresi")
    coefs = pd.DataFrame({"Fitur": features, "Koefisien": model.coef_}).sort_values("Koefisien", key=abs, ascending=False)
    st.dataframe(coefs)

    return model

def prediction_form(model):
    st.header("🎛️ E. Prediksi Manual")
    st.sidebar.header("📊 Input Manual")
    manual_input = {}
    for f in features:
        manual_input[f] = st.sidebar.number_input(f.replace("_", " ").title(), min_value=0.0, value=1000.0)
    input_df = pd.DataFrame([manual_input])
    prediction_result = model.predict(input_df)[0]
    st.sidebar.subheader("📌 Hasil Prediksi")
    st.sidebar.success(f"{prediction_result:.2f} MW")

# ============ Sidebar Navigasi ============ #
st.sidebar.title("🔍 Navigasi")
page = st.sidebar.radio("Pilih Halaman", [
    "📊 EDA & Visualisasi", "🔗 Korelasi", "🧠 Model & Evaluasi", "🎛️ Prediksi Manual"
])

# ============ Halaman Berdasarkan Navigasi ============ #
if page == "📊 EDA & Visualisasi":
    show_eda(df)
elif page == "🔗 Korelasi":
    show_correlation(df)
elif page == "🧠 Model & Evaluasi":
    trained_model = train_model(df)
elif page == "🎛️ Prediksi Manual":
    trained_model = LinearRegression().fit(df[features], df[target])
    prediction_form(trained_model)
