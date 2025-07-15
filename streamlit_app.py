import streamlit as st

# ====== Konfigurasi Aplikasi ====== #
st.set_page_config(page_title="⚡ Dashboard Prediksi Listrik", layout="wide")

# ====== Sidebar Kustom ====== #
with st.sidebar:
    st.image("solar2.webp", use_container_width=True, caption="Energi Terbarukan")
    st.markdown("## ⚡ **Navigasi Dashboard**")
    st.markdown("Silakan pilih halaman untuk eksplorasi:")
    st.markdown("""
- 📥 Data Collection  
- 📊 EDA  
- 🔗 Korelasi  
- 📐 Model  
- 📏 Evaluasi  
- 🎛️ Prediksi Manual  
""")
    st.markdown("---")
    st.markdown("""
📘 *Disusun oleh:*  
- Izzuddin Akmal Daffani Ramadhan (23.11.5483)
- Ahmad Baihaqi (23.11.5497)  
- Hanjaya Hartono (23.11.5449) 
- Danang Wijayanto (23.11.5468)

📚 *Big Data & Predictive Analytics*  
🏫 Universitas Amikom Yogyakarta
""")

# ====== Halaman Utama (Landing Page) ====== #
st.title("⚡ Dashboard Prediksi Permintaan Listrik")

st.markdown("""
Selamat datang di **Dashboard Analisis Permintaan Listrik Inggris & Wales Tahun 2024**.  
Dashboard ini bertujuan untuk mengeksplorasi, menganalisis, dan memprediksi permintaan listrik berdasarkan data historis.
""")

# ====== Ilustrasi Energi ====== #
st.image(
    "solar2.webp",
    caption="Panel Surya & Turbin Angin — Energi Terbarukan",
    use_container_width=True
)

# ====== Navigasi ====== #
st.markdown("---")
st.markdown("### 🧭 Navigasi Halaman:")
st.markdown("""
1. 📥 **Data Collection** — Deskripsi dan pembersihan dataset  
2. 📊 **EDA & Visualisasi Data** — Eksplorasi fitur dan distribusi  
3. 🔗 **Analisis Korelasi** — Hubungan antar fitur & target  
4. 📐 **Model Regresi Linier** — Pelatihan model prediktif  
5. 📏 **Evaluasi Model** — Akurasi dan performa model  
6. 🎛️ **Prediksi Manual** — Prediksi permintaan berdasarkan input pengguna
""")
st.markdown("---")

# ====== Penutup ====== #
st.markdown("""
🎓 *Proyek ini dikembangkan sebagai bagian dari tugas akhir mata kuliah Big Data.*  
Silakan jelajahi tiap menu untuk memahami proses prediksi permintaan listrik berbasis data historis.
""")
