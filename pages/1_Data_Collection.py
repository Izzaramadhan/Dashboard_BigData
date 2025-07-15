import streamlit as st
import pandas as pd

# ====== Konfigurasi Halaman ====== #
st.set_page_config(page_title="📥 Data Collection", layout="wide")
st.title("📥 A. Data Collection")

# ====== Load Dataset ====== #
df = pd.read_csv("historic_demand_2000 (1).csv")

# ====== Sumber Data ====== #
st.subheader("🗂️ Sumber Data")
st.markdown("""
Dataset yang digunakan merupakan data historis permintaan listrik di wilayah **Inggris dan Wales**,  
dengan fokus pada permintaan, pembangkitan energi terbarukan, serta interkoneksi lintas wilayah.

**Detail:**
- 🗂️ Nama file: `historic_demand_2000 (1).csv`  
- 🌐 Sumber: [Kaggle Datasets](https://www.kaggle.com/datasets?fileType=csv/)  
- 📄 Format: CSV  
- 🔢 Jumlah fitur: **13 fitur input + 1 target output**
""")

# ====== Deskripsi Fitur ====== #
st.subheader("📄 Deskripsi Fitur")
st.markdown("""
Beberapa fitur penting dalam dataset:

- `embedded_wind_generation`: Energi dari pembangkit angin  
- `embedded_solar_generation`: Energi dari pembangkit surya  
- `scottish_transfer`: Transfer listrik dari Skotlandia  
- Interkoneksi lainnya:
    - `ifa_flow`, `ifa2_flow`, `britned_flow`, `moyle_flow`,  
      `east_west_flow`, `nemo_flow`, `nsl_flow`, `eleclink_flow`,  
      `viking_flow`, `greenlink_flow`  
- `england_wales_demand`: **Target** — Total permintaan listrik (MW)
""")

# ====== Preview Dataset ====== #
st.subheader("📊 Preview Dataset")
st.dataframe(df.head(), use_container_width=True)

# ====== Fitur Unduh Dataset ====== #
st.subheader("⬇️ Unduh Dataset")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="historic_demand_clean.csv",
    mime="text/csv"
)
