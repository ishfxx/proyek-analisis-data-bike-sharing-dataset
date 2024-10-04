import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set judul aplikasi
st.title("Analisis Data Penyewaan Sepeda")

# Jalur file untuk day.csv dan hour.csv
day_file_path = '../data/day.csv'  # Sesuaikan jalur ini sesuai kebutuhan
hour_file_path = '../data/hour.csv'  # Sesuaikan jalur ini sesuai kebutuhan

# Memuat dataset
day_df = pd.read_csv(day_file_path)
hour_df = pd.read_csv(hour_file_path)

# Menampilkan beberapa baris pertama dari dataset
st.subheader("Prabaca Data")
st.write("5 baris pertama dari day.csv")
st.dataframe(day_df.head())
st.write("5 baris pertama dari hour.csv")
st.dataframe(hour_df.head())

# Memeriksa nilai yang hilang
st.subheader("Pemeriksaan Nilai yang Hilang")
st.write("Nilai yang hilang di day.csv:")
st.write(day_df.isnull().sum())
st.write("Nilai yang hilang di hour.csv:")
st.write(hour_df.isnull().sum())

# Memeriksa tipe data
st.subheader("Tipe Data dan Ringkasan")
st.write("Ringkasan untuk day.csv:")
st.write(day_df.info())
st.write("Ringkasan untuk hour.csv:")
st.write(hour_df.info())

# Membersihkan data
day_df.drop_duplicates(inplace=True)
hour_df.drop_duplicates(inplace=True)
day_df['season'] = day_df['season'].astype('category')
hour_df['season'] = hour_df['season'].astype('category')

# Menampilkan matriks korelasi
st.subheader("Matriks Korelasi")

fig, axes = plt.subplots(2, 1, figsize=(10, 12))
numerical_cols_day = day_df.select_dtypes(include=['float64', 'int64'])
numerical_cols_hour = hour_df.select_dtypes(include=['float64', 'int64'])

sns.heatmap(numerical_cols_day.corr(), annot=True, cmap='coolwarm', ax=axes[0])
axes[0].set_title('Matriks Korelasi - day.csv')

sns.heatmap(numerical_cols_hour.corr(), annot=True, cmap='coolwarm', ax=axes[1])
axes[1].set_title('Matriks Korelasi - hour.csv')

plt.tight_layout()
st.pyplot(fig)

# Plot batang untuk penyewaan sepeda berdasarkan musim
st.subheader("Penyewaan Sepeda berdasarkan Musim")
season_counts = day_df.groupby('season')['cnt'].sum().reset_index()
max_value = season_counts['cnt'].max()
season_counts['color'] = season_counts['cnt'].apply(lambda x: 'red' if x == max_value else 'pink')

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(season_counts['season'], season_counts['cnt'], color=season_counts['color'])
ax.set_title('Penyewaan Sepeda berdasarkan Musim (day.csv)')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penyewaan Sepeda')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')

st.pyplot(fig)

# Plot pencar untuk suhu vs penyewaan
st.subheader('Hubungan Suhu dan Jumlah Penyewaan Sepeda (day.csv)')

# Membuat hexbin plot
fig, ax = plt.subplots(figsize=(10, 6))
hb = ax.hexbin(day_df['temp'], day_df['cnt'], gridsize=15, cmap='Blues', mincnt=1)

# Menambahkan colorbar
cb = fig.colorbar(hb, ax=ax, label='Jumlah Titik')

# Tambahkan label sumbu
ax.set_xlabel('Suhu', fontsize=14)
ax.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=14)

# Tampilkan plot di Streamlit
st.pyplot(fig)

st.subheader('Pola penyewaan sepeda berdasarkan jam (day.csv)')
# Plot penyewaan per jam
max_rentals = hour_df['cnt'].max()
max_hour = hour_df.loc[hour_df['cnt'] == max_rentals, 'hr'].values[0]

# Membuat plot histogram
plt.figure(figsize=(12, 6))

# Membuat histogram untuk data biasa
plt.bar(hour_df['hr'][hour_df['cnt'] < max_rentals], 
         hour_df['cnt'][hour_df['cnt'] < max_rentals], 
         color='pink', alpha=0.7, width=0.6)

# Membuat histogram untuk data tertinggi
plt.bar(max_hour, max_rentals, 
         color='red', alpha=0.9, width=0.6, label=f'Maks Penyewaan ({max_rentals})')

# Menambahkan judul dan label
plt.title('Pola Penyewaan Sepeda Berdasarkan Jam (hour.csv)', fontsize=16, fontweight='bold')
plt.xlabel('Jam', fontsize=14)
plt.ylabel('Jumlah Penyewaan', fontsize=14)

# Menampilkan grid
plt.grid(axis='y')

# Menampilkan legenda
plt.legend()

# Menampilkan plot di Streamlit
st.pyplot(plt)

# Analisis kondisi cuaca
st.subheader("Dampak Kondisi Cuaca terhadap Penyewaan")
weather_counts = day_df.groupby('weathersit')['cnt'].sum().reset_index()
max_count = weather_counts['cnt'].max()

fig, ax = plt.subplots(figsize=(10, 6))
for index, row in weather_counts.iterrows():
    color = 'blue' if row['cnt'] == max_count else 'lightblue'
    ax.bar(row['weathersit'], row['cnt'], color=color)

ax.set_title('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda (day.csv)', fontsize=16)
ax.set_xlabel('Kondisi Cuaca', fontsize=14)
ax.set_ylabel('Total Penyewaan Sepeda', fontsize=14)
ax.grid(axis='y')

st.pyplot(fig)
