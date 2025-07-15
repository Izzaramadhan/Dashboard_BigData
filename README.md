# ⚡ Dashboard Prediksi Permintaan Listrik - Big Data Final Project

Proyek ini merupakan implementasi **analisis data dan prediksi permintaan listrik** di Inggris & Wales menggunakan model **Regresi Linier Berganda**, dikemas dalam dashboard interaktif berbasis **Streamlit**.

## 📁 Struktur Proyek

fpbigdata/
├── historic_demand_2000 (1).csv # Dataset asli
├── pages/
│ ├── 1_Data_Collection.py # Halaman pengumpulan dan pembersihan data
│ ├── 2_EDA.py # Exploratory Data Analysis
│ ├── 3_Korelasi.py # Analisis Korelasi antar fitur
│ ├── 4_Model.py # Pelatihan model regresi
│ ├── 5_Evaluasi.py # Evaluasi kinerja model
│ └── 6_Prediksi.py # Prediksi manual dengan input user
├── streamlit_app.py # Halaman landing dashboard
├── requirements.txt # Daftar dependensi
└── README.md # Dokumentasi proyek

## 📊 Fitur Dashboard

Dashboard terbagi menjadi beberapa halaman (navigasi via sidebar):

### A. Data Collection
- Penjelasan sumber dataset
- Deskripsi fitur dan target
- Preview dan opsi unduh dataset (CSV)

### B. EDA & Visualisasi
- Statistik ringkas permintaan listrik
- Histogram distribusi demand
- Scatter plot wind vs solar
- Rata-rata output vs permintaan

### C. Analisis Korelasi
- Heatmap interaktif (Plotly)
- Heatmap statik (Seaborn)
- Interpretasi kekuatan korelasi fitur

### D. Model Regresi Linier
- Pembagian data train-test
- Pelatihan model regresi
- Koefisien tiap fitur

### E. Evaluasi Model
- MAE, RMSE, MSE, dan R²
- Visualisasi Prediksi vs Aktual (Line & Scatter)

### F. Prediksi Manual
- Input semua fitur secara manual via sidebar
- Prediksi realtime + error bar (berdasarkan RMSE)
- Grafik batang + batas prediksi

---

## ⚙️ Cara Menjalankan

1. **Clone repository**:
   ```bash
   git clone https://github.com/username/fpbigdata.git
   cd fpbigdata
Aktifkan virtual environment:

python -m venv venv
venv\Scripts\activate  # Untuk Windows
# atau
source venv/bin/activate  # Untuk macOS/Linux
Instal dependensi:


pip install -r requirements.txt
Jalankan aplikasi Streamlit:


streamlit run streamlit_app.py
📦 Requirements
Daftar dependensi yang digunakan:

streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
plotly
statsmodels
Semua tercantum di dalam requirements.txt.

📂 Dataset
📄 File: historic_demand_2000 (1).csv

🌐 Sumber: Kaggle Datasets

Fitur: Embedded wind/solar generation, transfer antar negara, demand

📜 Lisensi
Proyek ini dibuat untuk keperluan akademik dalam mata kuliah Big Data & Predictive Analytics.
Boleh dimodifikasi dan digunakan kembali untuk pembelajaran.
