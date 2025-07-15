import streamlit as st
import pandas as pd
import plotly.express as px

# ====== Pengaturan Halaman ====== #
st.set_page_config(page_title="📊 EDA & Visualisasi", layout="wide")
st.title("📊 B. EDA dan Visualisasi Data")

# ====== Load Data ====== #
df = pd.read_csv('historic_demand_2000 (1).csv')
target = 'england_wales_demand'

# ====== Info Ukuran Dataset ====== #
st.markdown(f"📏 Dataset berisi **{df.shape[0]:,} baris** dan **{df.shape[1]} kolom.**")

# ====== Statistik Ringkas ====== #
st.subheader("📌 Statistik Deskriptif Target (Demand)")
col1, col2, col3 = st.columns(3)
col1.metric("Rata-rata Demand", f"{df[target].mean():,.2f} MW")
col2.metric("Maksimum Demand", f"{df[target].max():,.2f} MW")
col3.metric("Minimum Demand", f"{df[target].min():,.2f} MW")

# ====== Statistik Lengkap (expandable) ====== #
with st.expander("📄 Lihat Statistik Lengkap (describe)"):
    st.dataframe(df.describe().round(2), use_container_width=True)

# ====== Distribusi Target ====== #
st.subheader("📈 Distribusi Permintaan Listrik")
log_scale = st.checkbox("Gunakan Log Scale", value=False)
fig1 = px.histogram(
    df, x=target, nbins=30,
    title="Distribusi Permintaan Listrik (MW)",
    log_y=log_scale,
    color_discrete_sequence=['#1f77b4']
)
st.plotly_chart(fig1, use_container_width=True)

# ====== Korelasi Fitur Visual ====== #
st.subheader("🌤️ Scatter Plot Wind vs Solar Generation")
fig2 = px.scatter(
    df, x='embedded_wind_generation', y='embedded_solar_generation',
    title="Hubungan Embedded Wind vs Solar Generation",
    labels={
        'embedded_wind_generation': 'Embedded Wind (MW)',
        'embedded_solar_generation': 'Embedded Solar (MW)'
    },
    color_discrete_sequence=['#2ca02c']
)
st.plotly_chart(fig2, use_container_width=True)

# ====== Rata-rata Output vs Demand ====== #
st.subheader("🔋 Perbandingan Rata-rata Output vs Permintaan")
avg_data = {
    'Embedded Wind': df['embedded_wind_generation'].mean(),
    'Embedded Solar': df['embedded_solar_generation'].mean(),
    'Demand': df[target].mean()
}
avg_df = pd.DataFrame(avg_data.items(), columns=['Kategori', 'Rata-rata (MW)'])
fig_bar = px.bar(
    avg_df, x='Kategori', y='Rata-rata (MW)', color='Kategori',
    title='Perbandingan Rata-rata Output (Wind & Solar) vs Permintaan',
    text_auto='.2s',
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig_bar, use_container_width=True)

# ====== Penutup ====== #
st.success("✅ Data berhasil divisualisasikan. Gunakan ini sebagai langkah awal eksplorasi.")
