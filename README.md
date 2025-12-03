# Analisis Sentimen & Klasifikasi Teks

Aplikasi ini menggunakan Machine Learning (Random Forest) untuk klasifikasi teks dengan preprocessing khusus Bahasa Indonesia (Sastrawi) dan penanganan data tidak seimbang menggunakan SMOTE. Web server dibangun menggunakan Flask.

## ⚙️ Persyaratan Sistem

Pastikan **Python** sudah terinstal di komputer Anda.

### 1. Instalasi Library
Buka Terminal atau CMD di folder project, lalu jalankan perintah berikut untuk menginstall library yang dibutuhkan:

```bash
pip install pandas nltk Sastrawi scikit-learn matplotlib imbalanced-learn flask joblib
2. Download Data NLTK
Aplikasi membutuhkan corpus tambahan (stopwords dan tokenizer). Jalankan script python berikut sekali saja sebelum memulai:

Python

import nltk
nltk.download('stopwords')
nltk.download('punkt')
🚀 Cara Menjalankan (How to Run)
Ikuti urutan langkah berikut agar aplikasi berjalan dengan benar:

Langkah 1: Training Model (Wajib)
Jalankan file Jupyter Notebook (.ipynb) terlebih dahulu sebelum menjalankan website.

Buka file .ipynb yang ada di repository ini.

Jalankan semua cell (Run All).

Proses ini akan menghasilkan file model (.pkl) yang dibutuhkan oleh aplikasi.

Langkah 2: Jalankan Aplikasi Web
Setelah file model .pkl terbentuk:

Buka Terminal/CMD.

Jalankan file aplikasi Python:

Bash

python app.py
(Sesuaikan app.py dengan nama file utama kamu)

Buka browser dan akses alamat localhost yang muncul (biasanya http://127.0.0.1:5000).

Tech Stack & Library
Language: Python

Web Framework: Flask

Data Processing: Pandas, NumPy

NLP (Natural Language Processing):

NLTK (Tokenization, Stopwords)

Sastrawi (Stemming Bahasa Indonesia)

Machine Learning:

Scikit-Learn (Random Forest Classifier, TF-IDF, CountVectorizer)

Imbalanced-learn (SMOTE untuk oversampling data)

Utilities: Joblib (Model loading/saving), Matplotlib (Visualisasi)
