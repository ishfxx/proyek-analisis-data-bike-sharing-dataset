# Proyek Analisis Data: Tren Penyewaan Sepeda: Mengkaji Pengaruh Suhu dan Hari Libur pada Pengguna Kasual 🚴‍♂️

Proyek bertujuan untuk mengeksplorasi faktor-faktor yang memengaruhi penyewaan sepeda, termasuk musim dengan jumlah penyewaan tertinggi, pengaruh suhu terhadap penyewaan harian dan per jam, serta dampak kondisi cuaca terhadap total penyewaan sepeda, melalui visualisasi bar plot, scatter plot, dan line plot untuk mengidentifikasi pola dan hubungan signifikan.

## Fitur Utama 🚀

- **Pertanyaan Bisnis**: Proyek ini fokus pada empat pertanyaan utama:
  - Musim apa yang memiliki jumlah penyewaan sepeda tertinggi?
  - Bagaimana suhu memengaruhi jumlah penyewaan sepeda harian?
  - Bagaimana suhu memengaruhi penyewaan sepeda pada jam tertentu?
  - Bagaimana kondisi cuaca memengaruhi total penyewaan sepeda?
- **Import Data & Wrangling**: Proses memuat, menilai, dan membersihkan data dilakukan secara bertahap, termasuk penghapusan kolom yang tidak diperlukan.
- **Exploratory Data Analysis (EDA)**: Bertujuan untuk mengeksplorasi faktor-faktor yang memengaruhi penyewaan sepeda, termasuk musim dengan jumlah penyewaan tertinggi, pengaruh suhu terhadap penyewaan harian dan per jam, serta dampak kondisi cuaca terhadap total penyewaan sepeda, melalui visualisasi bar plot, scatter plot, dan line plot untuk mengidentifikasi pola dan hubungan signifikan.

- **Regresi Linear**: Proyek ini melakukan analisis regresi linear untuk memodelkan hubungan antara suhu dan jumlah penyewa sepeda harian.

- **Visualisasi Interaktif**: Menggunakan **Streamlit** untuk menghasilkan visualisasi dan analisis interaktif.

## Struktur Proyek 📂

Proyek ini terdiri dari beberapa file dan direktori:

- `notebook.ipynb`: Jupyter Notebook yang berisi analisis mendalam terkait tren penyewaan sepeda.
- `data/`: Direktori yang berisi dataset penyewaan sepeda.
  - `day.csv`: Dataset penyewaan sepeda harian.
  - `hour.csv`: Dataset penyewaan sepeda per jam.
- `dashboard.py`: Script Python untuk menjalankan dashboard interaktif menggunakan **Streamlit**.
- `README.md`: Dokumentasi proyek ini.
- `requirements.txt`: Daftar pustaka Python yang diperlukan untuk menjalankan proyek ini.

## Cara Menjalankan Proyek 💻

### 1. Menjalankan Jupyter Notebook

Untuk menjalankan analisis di **Jupyter Notebook**:

1. Pastikan semua dependensi sudah terpasang dengan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

### 2. Menjalankan Dasbor Streamlit

Proyek ini juga menyediakan dashboard interaktif menggunakan **Streamlit**. Ikuti langkah berikut untuk menjalankannya:

1. Instal semua dependensi menggunakan:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi **Streamlit**:
   ```bash
   streamlit run dashboard.py
   ```

## Insight Utama 📊

1. **Musim apa yang memiliki jumlah penyewaan sepeda tertinggi**:

   - Musim memiliki pengaruh signifikan terhadap jumlah penyewaan sepeda. Musim panas atau musim semi, di mana kondisi cuaca lebih kondusif untuk bersepeda, cenderung menunjukkan peningkatan jumlah penyewaan sepeda. Perusahaan dapat fokus meningkatkan stok sepeda dan melakukan promosi selama musim-musim dengan permintaan tinggi, seperti musim panas. Sebaliknya, pada musim dingin atau musim hujan, promosi khusus atau penyesuaian layanan mungkin diperlukan untuk menarik pelanggan.

2. **Bagaimana suhu memengaruhi jumlah penyewaan sepeda harian**:

   - Suhu harian memengaruhi tingkat penyewaan sepeda. Pada hari-hari dengan suhu yang lebih hangat (tidak terlalu panas atau dingin), penyewaan cenderung meningkat. Ini menunjukkan bahwa kondisi iklim sedang lebih menarik bagi pelanggan. Untuk perusahaan, penting untuk menyiapkan strategi yang fleksibel berdasarkan prediksi cuaca, seperti menawarkan diskon pada hari-hari yang kurang ideal, atau memberikan layanan ekstra pada hari-hari dengan suhu yang lebih nyaman.

3. **Bagaimana suhu memengaruhi penyewaan sepeda pada jam tertentu**:

   - Penyewaan sepeda cenderung meningkat pada jam-jam sibuk (misalnya pagi dan sore) ketika suhu berada pada tingkat yang nyaman. Hal ini menunjukkan bahwa selain suhu, aktivitas rutin pelanggan (seperti berangkat atau pulang kerja) juga memengaruhi pola penyewaan. Perusahaan dapat meningkatkan jumlah sepeda yang tersedia dan promosi selama jam-jam tersebut untuk memaksimalkan keuntungan. Pada jam-jam yang lebih dingin atau panas, layanan penyesuaian mungkin diperlukan.

4. **Bagaimana kondisi cuaca memengaruhi total penyewaan sepeda**:
   - Cuaca buruk seperti hujan atau kabut cenderung menyebabkan penurunan penyewaan sepeda. Cuaca cerah dan stabil mendukung jumlah penyewaan yang lebih tinggi. Oleh karena itu, perusahaan perlu merancang strategi untuk mengantisipasi cuaca buruk, seperti menawarkan promosi khusus atau memberikan layanan perlengkapan cuaca (misalnya jas hujan atau penutup sepeda) agar tetap menarik bagi pelanggan dalam kondisi cuaca yang tidak ideal.

## Dataset

Dataset yang digunakan dalam proyek ini adalah:

- **day.csv**: Dataset harian yang mencatat data penyewaan sepeda termasuk informasi tentang suhu, kondisi cuaca, dan status hari libur.
- **hour.csv**: Dataset per jam yang mencatat data penyewaan sepeda per jam, memberikan detail yang lebih spesifik terkait waktu.

## Library yang Digunakan

- **Python**: Bahasa pemrograman yang digunakan untuk analisis dan visualisasi data.
- **Streamlit**: Library Python untuk membuat aplikasi web interaktif.
- **Matplotlib & Seaborn**: Digunakan untuk visualisasi data.
- **Pandas**: pustaka sumber terbuka yang digunakan untuk analisis dan manipulasi data.
- **Seaborn**: pustaka visualisasi data Python yang berbasis pada matplotlib
