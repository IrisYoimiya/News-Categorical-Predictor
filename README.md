# Analisis Sentimen & Klasifikasi Teks

Aplikasi ini menggunakan Machine Learning (Random Forest) untuk klasifikasi teks dengan preprocessing khusus Bahasa Indonesia (Sastrawi) dan penanganan data tidak seimbang menggunakan SMOTE. Web server dibangun menggunakan Flask.

## Persyaratan Sistem

Pastikan **Python** sudah terinstal di komputer Anda.

### 1. Instalasi Library
Buka Terminal atau CMD di folder project, lalu jalankan perintah berikut untuk menginstall library yang dibutuhkan:

```bash
pip install pandas nltk Sastrawi scikit-learn matplotlib imbalanced-learn flask joblib

### 2. Download Data NLTK
Aplikasi membutuhkan corpus tambahan (stopwords dan tokenizer). Jalankan script python berikut sekali saja sebelum memulai:
import nltk
nltk.download('stopwords')
nltk.download('punkt')

Cara Menjalankan (How to Run)
Ikuti urutan langkah berikut agar aplikasi berjalan dengan benar:

Langkah 1: Training Model (Wajib)
Jalankan file Jupyter Notebook (.ipynb) terlebih dahulu sebelum menjalankan website.

Buka file .ipynb yang ada di repository ini.

Jalankan semua cell (Run All).

Proses ini akan menghasilkan file model yang dibutuhkan oleh aplikasi.

Langkah 2: Jalankan Aplikasi Web
Setelah file model terbentuk:

Buka Terminal/CMD.

Jalankan file aplikasi Python:
python deploy.py
Buka browser dan akses alamat localhost yang muncul
