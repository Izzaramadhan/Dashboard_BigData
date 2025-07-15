import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import plotly.express as px

# ====== Pengaturan Halaman ====== #
st.set_page_config(page_title="📐 Model Regresi", layout="wide")
st.title("📐 D. Membuat Model Regresi Linier")

# ====== Load Data ====== #
df = pd.read_csv('historic_demand_2000 (1).csv')
target = 'england_wales_demand'
features = [
    'embedded_wind_generation', 'embedded_solar_generation', 'scottish_transfer',
    'ifa_flow', 'ifa2_flow', 'britned_flow', 'moyle_flow', 'east_west_flow',
    'nemo_flow', 'nsl_flow', 'eleclink_flow', 'viking_flow', 'greenlink_flow'
]

# ====== Preview Data ====== #
with st.expander("🔍 Preview Data Fitur dan Target"):
    st.write("📄 Data Fitur (X)")
    st.dataframe(df[features].head(), use_container_width=True)
    st.write("🎯 Target (y)")
    st.dataframe(df[[target]].head(), use_container_width=True)

# ====== Split Dataset ====== #
st.subheader("📊 Pembagian Data Latih dan Uji")
X = df[features]
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

st.markdown(f"""
- 📚 Jumlah data latih: **{X_train.shape[0]} baris**  
- 🧪 Jumlah data uji: **{X_test.shape[0]} baris**
""")

# ====== Pelatihan Model ====== #
st.subheader("🧠 Melatih Model Regresi Linier")

with st.spinner("Melatih model..."):
    model = LinearRegression()
    model.fit(X_train, y_train)

st.success("✅ Model berhasil dilatih!")

# ====== Informasi Model ====== #
st.subheader("📈 Informasi Model")
st.markdown(f"""
- **Intercept (Bias):** `{model.intercept_:.2f}`  
- **R² Score (Training Set):** `{r2_score(y_train, model.predict(X_train)):.4f}`
""")

# ====== Menampilkan Koefisien ====== #
st.subheader("📉 Koefisien Regresi")
coef_df = pd.DataFrame({
    "Fitur": features,
    "Koefisien": model.coef_
}).sort_values(by="Koefisien", key=abs, ascending=False)

st.dataframe(coef_df.style.format({"Koefisien": "{:.4f}"}), use_container_width=True)

# ====== Visualisasi Koefisien ====== #
st.subheader("📊 Visualisasi Pengaruh Fitur")
fig = px.bar(coef_df, x='Fitur', y='Koefisien', title="Pengaruh Fitur terhadap Target (Koefisien Regresi)",
             text_auto=".2f", color='Koefisien', color_continuous_scale='RdBu')
fig.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig, use_container_width=True)

# ====== Interpretasi ====== #
st.markdown("""
> Koefisien menunjukkan arah dan kekuatan pengaruh fitur terhadap permintaan listrik:
- Koefisien **positif** ➜ menaikkan demand
- Koefisien **negatif** ➜ menurunkan demand  
Semakin besar nilai absolutnya, semakin besar pengaruhnya terhadap output.
""")
