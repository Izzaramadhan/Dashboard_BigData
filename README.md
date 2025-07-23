# ⚡ Dashboard Prediksi Permintaan Listrik - Big Data Final Project

Proyek ini merupakan implementasi **analisis data dan prediksi permintaan listrik** di Inggris & Wales menggunakan model **Regresi Linier Berganda**, dikemas dalam dashboard interaktif berbasis **Streamlit**.

---

## 📁 Struktur Proyek

```
fpbigdata/
├── historic_demand_2000 (1).csv       # Dataset asli
├── pages/
│   ├── 1_Data_Collection.py           # Halaman pengumpulan dan pembersihan data
│   ├── 2_EDA.py                       # Exploratory Data Analysis
│   ├── 3_Korelasi.py                  # Analisis Korelasi antar fitur
│   ├── 4_Model.py                     # Pelatihan model regresi
│   ├── 5_Evaluasi.py                  # Evaluasi kinerja model
│   └── 6_Prediksi.py                  # Prediksi manual dengan input user
├── streamlit_app.py                  # Halaman landing dashboard
├── requirements.txt                  # Daftar dependensi
└── README.md                         # Dokumentasi proyek
```

---

## 📊 Fitur Dashboard

Dashboard terbagi menjadi beberapa halaman (navigasi via sidebar):

### A. 📥 Data Collection
- Penjelasan sumber dataset
- Deskripsi fitur dan target
- Preview dan unduh dataset (CSV)

### B. 📊 EDA & Visualisasi
- Statistik ringkas permintaan listrik
- Histogram distribusi demand
- Scatter plot wind vs solar
- Rata-rata produksi vs permintaan

### C. 🔗 Analisis Korelasi
- Heatmap interaktif (Plotly)
- Heatmap statik (Seaborn)
- Interpretasi korelasi antar fitur dan target

### D. 📐 Model Regresi Linier
- Pembagian data latih dan uji
- Pelatihan model regresi linier berganda
- Tabel koefisien regresi tiap fitur

### E. 📏 Evaluasi Model
- Evaluasi dengan MAE, RMSE, MSE, dan R²
- Visualisasi prediksi vs data aktual

### F. 🎛️ Prediksi Manual
- Input manual semua fitur via sidebar
- Prediksi permintaan listrik real-time
- Visualisasi batang + error bar (berdasarkan RMSE)

---

## ⚙️ Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/username/fpbigdata.git
cd fpbigdata
```

### 2. Aktifkan Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# atau
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
```bash
streamlit run streamlit_app.py
```

---

## 📦 Requirements

Daftar dependensi:
- `streamlit`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `plotly`
- `statsmodels`

Tercantum lengkap dalam file `requirements.txt`.

---

## 📂 Dataset

- 📄 File: `historic_demand_2024.csv`  
- 🌐 Sumber: [Kaggle Datasets](https://www.kaggle.com/datasets)  
- 🧾 Fitur: Embedded wind/solar generation, transfer listrik, demand

---

## 📜 Lisensi

Proyek ini dibuat untuk keperluan akademik mata kuliah **Big Data & Predictive Analytics**.  
Bebas digunakan dan dimodifikasi untuk kepentingan pembelajaran.
