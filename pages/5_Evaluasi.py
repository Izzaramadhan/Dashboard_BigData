import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import plotly.express as px
import plotly.graph_objects as go

# ====== Pengaturan Halaman ====== #
st.set_page_config(page_title="📏 Evaluasi Model", layout="wide")
st.title("📏 E. Evaluasi Model Regresi Linier")

# ====== Load Data ====== #
df = pd.read_csv('historic_demand_2000 (1).csv')
target = 'england_wales_demand'
features = [
    'embedded_wind_generation', 'embedded_solar_generation', 'scottish_transfer',
    'ifa_flow', 'ifa2_flow', 'britned_flow', 'moyle_flow', 'east_west_flow',
    'nemo_flow', 'nsl_flow', 'eleclink_flow', 'viking_flow', 'greenlink_flow'
]

# ====== Split dan Latih Model ====== #
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)
y_train_pred = model.predict(X_train)

# ====== Evaluasi ====== #
st.subheader("📊 Hasil Evaluasi Model")

# Hitung metrik
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

train_r2 = r2_score(y_train, y_train_pred)

# Tampilkan metrik
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("MAE", f"{mae:.2f}")
col2.metric("RMSE", f"{rmse:.2f}")
col3.metric("MSE", f"{mse:.2f}")
col4.metric("R² Test", f"{r2:.4f}")
col5.metric("R² Train", f"{train_r2:.4f}")

# Penjelasan
st.markdown("""
- **MAE**: Rata-rata selisih absolut prediksi dan aktual  
- **RMSE**: Menghukum kesalahan besar lebih berat  
- **R²**: Seberapa baik fitur menjelaskan variabilitas target  
""")

# ====== Line Chart: Prediksi vs Aktual ====== #
st.subheader("📈 Prediksi vs Data Aktual")
chart_df = pd.DataFrame({
    "Aktual": y_test.values[:100],
    "Prediksi": y_pred[:100]
})
fig_line = px.line(chart_df, title="📊 100 Data Pertama — Aktual vs Prediksi",
                   labels={"value": "Demand (MW)", "index": "Index"})
st.plotly_chart(fig_line, use_container_width=True)

# ====== Scatter Plot: Aktual vs Prediksi ====== #
st.subheader("📉 Scatter Plot: Aktual vs Prediksi")
fig_scatter = px.scatter(x=y_test, y=y_pred, labels={'x': 'Aktual', 'y': 'Prediksi'},
                         title="Scatter Plot Prediksi vs Aktual", trendline="ols")
st.plotly_chart(fig_scatter, use_container_width=True)

# ====== Residuals Plot ====== #
st.subheader("📉 Visualisasi Error (Residuals)")
residuals = y_test - y_pred
fig_resid = px.scatter(x=y_pred, y=residuals,
                       labels={'x': 'Prediksi', 'y': 'Error (Residual)'},
                       title="Residuals vs Prediksi")
fig_resid.add_hline(y=0, line_dash="dot", line_color="red")
st.plotly_chart(fig_resid, use_container_width=True)

# ====== Histogram Error ====== #
st.subheader("📊 Distribusi Error")
fig_hist = px.histogram(residuals, nbins=40, title="Distribusi Residual Error",
                        labels={'value': 'Error (MW)'})
st.plotly_chart(fig_hist, use_container_width=True)

# ====== Interpretasi ====== #
st.markdown("""
> Jika distribusi error mendekati normal dan residual tersebar merata di sekitar nol,  
itu menunjukkan model sudah cukup baik.  
Namun jika R² rendah atau residual besar, maka perlu pertimbangkan:
- Transformasi fitur
- Tambah fitur baru
- Coba model non-linier
""")

st.success("✅ Evaluasi model berhasil dilakukan dengan lengkap.")
