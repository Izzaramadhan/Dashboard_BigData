import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# ========== KONFIGURASI HALAMAN ========== #
st.set_page_config(page_title="🎛️ Prediksi Manual", layout="wide")
st.title("🎛️ F. Prediksi Manual Permintaan Listrik")

# ========== LOAD DATA ========== #
df = pd.read_csv('historic_demand_2000 (1).csv')

features = [
    'embedded_wind_generation', 'embedded_solar_generation', 'scottish_transfer',
    'ifa_flow', 'ifa2_flow', 'britned_flow', 'moyle_flow', 'east_west_flow',
    'nemo_flow', 'nsl_flow', 'eleclink_flow', 'viking_flow', 'greenlink_flow'
]
target = 'england_wales_demand'

# ========== INPUT MANUAL ========== #
st.sidebar.header("🧾 Input Data Manual")
manual_input = {
    f: st.sidebar.number_input(f.replace("_", " ").title(), min_value=0.0, value=1000.0, step=100.0)
    for f in features
}
input_df = pd.DataFrame([manual_input])

# ========== LATIH MODEL ========== #
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# ========== PREDIKSI & ERROR BAR ========== #
prediction = model.predict(input_df)[0]
y_pred_test = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
lower_bound = prediction - rmse
upper_bound = prediction + rmse

# ========== TAMPILKAN HASIL ========== #
st.sidebar.subheader("📌 Hasil Prediksi")
st.sidebar.success(f"{prediction:.2f} MW")
st.sidebar.markdown(f"📉 *Estimasi Error: ±{rmse:.2f} MW*")

# ========== TAMPILKAN INPUT PENGGUNA ========== #
st.subheader("📋 Data Input Pengguna")
st.dataframe(input_df.T.rename(columns={0: "Nilai Input"}), use_container_width=True)

# ========== VISUALISASI ========== #
st.subheader("📊 Visualisasi Prediksi dengan Error Bar")
fig = go.Figure()

fig.add_trace(go.Bar(
    x=["Permintaan Listrik (Prediksi)"],
    y=[prediction],
    name="Prediksi",
    error_y=dict(
        type='data',
        array=[rmse],
        visible=True
    ),
    marker_color='lightskyblue'
))

fig.update_layout(
    title="Prediksi Permintaan Listrik & Error Bar",
    yaxis_title="Demand (MW)",
    height=400
)

st.plotly_chart(fig, use_container_width=True)

st.markdown(f"""
> Grafik di atas memperlihatkan hasil prediksi permintaan listrik berdasarkan input pengguna,  
dilengkapi dengan *error bar* ±{rmse:.2f} MW sebagai estimasi ketidakpastian model berdasarkan performa pada data uji.
""")
