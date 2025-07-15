# ⚡ Dashboard Prediksi Permintaan Listrik - Big Data Final Project

Proyek ini merupakan implementasi analisis data dan prediksi permintaan listrik di Inggris & Wales menggunakan model **Regresi Linier Berganda**, dilengkapi dengan dashboard interaktif berbasis **Streamlit**.

## 📁 Struktur Proyek

```
fpbigdata/
├── historic_demand_2000 (1).csv
├── streamlit_app_modular_fixed.py
├── venv/
└── README.md
```

## 📊 Fitur Dashboard

Dashboard terbagi menjadi beberapa halaman interaktif:

### A. EDA dan Visualisasi Data
- Tinjauan data mentah
- Distribusi permintaan listrik
- Scatter plot Wind vs Solar
- Rata-rata energi vs permintaan

### B. Analisis Korelasi
- Heatmap interaktif antar fitur
- Korelasi statistik antar variabel

### C. Regresi Linier Berganda
- Pelatihan model prediksi
- Evaluasi dengan MSE, RMSE, MAE, dan R²
- Visualisasi Prediksi vs Aktual

### D. Prediksi Manual
- Input manual untuk semua fitur
- Hasil prediksi permintaan listrik secara instan

## ⚙️ Cara Menjalankan

1. **Clone repository**:
   ```bash
   git clone https://github.com/username/namarepo.git
   cd namarepo
   ```

2. **Buat virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan dashboard**:
   ```bash
   streamlit run streamlit_app.py
   ```

## 📦 Requirements

Lihat `requirements.txt` untuk dependensi.

## 📜 Lisensi

Proyek ini untuk keperluan akademik. Gunakan dan modifikasi sesuai kebutuhan pembelajaran.