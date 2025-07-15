import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

# ====== Pengaturan Halaman ====== #
st.set_page_config(page_title="🔗 Korelasi", layout="wide")
st.title("🔗 C. Analisis Korelasi")

# ====== Load Data ====== #
df = pd.read_csv('historic_demand_2000 (1).csv')
target = 'england_wales_demand'
features = [
    'embedded_wind_generation', 'embedded_solar_generation', 'scottish_transfer',
    'ifa_flow', 'ifa2_flow', 'britned_flow', 'moyle_flow', 'east_west_flow',
    'nemo_flow', 'nsl_flow', 'eleclink_flow', 'viking_flow', 'greenlink_flow'
]

# ====== Korelasi ====== #
st.subheader("📌 Matriks Korelasi")
corr = df[features + [target]].corr().round(2)

tab1, tab2 = st.tabs(["🧭 Heatmap Interaktif", "📊 Heatmap Statik"])

with tab1:
    fig_interaktif = ff.create_annotated_heatmap(
        z=corr.values,
        x=list(corr.columns),
        y=list(corr.index),
        annotation_text=corr.values,
        colorscale='Viridis',
        showscale=True,
        hoverinfo="z"
    )
    st.plotly_chart(fig_interaktif, use_container_width=True)

with tab2:
    colormap = st.selectbox("🎨 Pilih Skema Warna:", ["coolwarm", "YlGnBu", "RdBu", "mako", "rocket"], index=0)
    fig_static, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap=colormap, ax=ax, fmt='.2f', linewidths=0.5, square=True)
    st.pyplot(fig_static)

# ====== Korelasi Terhadap Target ====== #
st.subheader("📈 Korelasi Terhadap Target (england_wales_demand)")
target_corr = corr[target].drop(target).sort_values(ascending=False).reset_index()
target_corr.columns = ['Fitur', 'Korelasi']
st.dataframe(target_corr.style.highlight_max(axis=0, color='lightgreen'), use_container_width=True)

# ====== Interpretasi Korelasi ====== #
st.subheader("📝 Interpretasi Korelasi")
st.markdown("""
- Nilai **korelasi positif** berarti fitur searah dengan permintaan listrik.
- Nilai **korelasi negatif** berarti fitur berbanding terbalik.
- Nilai korelasi mendekati **1 atau -1** berarti hubungan kuat.

📌 **Fitur dengan korelasi tertinggi terhadap demand:**  
- 🔼 **{}** (`{:.2f}`)  
📌 **Fitur dengan korelasi terendah:**  
- 🔽 **{}** (`{:.2f}`)
""".format(
    target_corr.iloc[0]['Fitur'], target_corr.iloc[0]['Korelasi'],
    target_corr.iloc[-1]['Fitur'], target_corr.iloc[-1]['Korelasi']
))

st.success("✅ Analisis korelasi selesai dilakukan.")
