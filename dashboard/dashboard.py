import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

# Checking missing values
st.header("Checking missing values for 'day.csv':")
st.write(day_df.isnull().sum())

st.header("Checking missing values for 'hour.csv':")
st.write(hour_df.isnull().sum())

# Data types and summary
st.header("Data types and summary for 'day.csv':")
st.write(day_df.info())

st.header("Data types and summary for 'hour.csv':")
st.write(hour_df.info())

# Drop duplicates
day_df.drop_duplicates(inplace=True)
hour_df.drop_duplicates(inplace=True)

# Convert columns to category type
day_df['season'] = day_df['season'].astype('category')
hour_df['season'] = hour_df['season'].astype('category')

# Display the first few rows of the cleaned data
st.subheader("Cleaned Data - day.csv (5 rows):")
st.write(day_df.head())

st.subheader("Cleaned Data - hour.csv (5 rows):")
st.write(hour_df.head())

# Select numerical columns for correlation matrix
numerical_cols_day = day_df.select_dtypes(include=['float64', 'int64'])
numerical_cols_hour = hour_df.select_dtypes(include=['float64', 'int64'])

# Plot correlation matrices
st.header("Correlation Matrices")

fig, axes = plt.subplots(2, 1, figsize=(10, 12))  

sns.heatmap(numerical_cols_day.corr(), annot=True, cmap='coolwarm', ax=axes[0])
axes[0].set_title('Correlation Matrix - day.csv')

sns.heatmap(numerical_cols_hour.corr(), annot=True, cmap='coolwarm', ax=axes[1])
axes[1].set_title('Correlation Matrix - hour.csv')

st.pyplot(fig)

# Read the day.csv again (if needed)
day_df = pd.read_csv('C:/Users/NABIL/Documents/Tugas Matkul/Bangkit/Dicoding/submission/data/day.csv')

# Bar plot for season-wise rentals
season_counts = day_df.groupby('season')['cnt'].sum().reset_index()
max_value = season_counts['cnt'].max()
season_counts['color'] = season_counts['cnt'].apply(lambda x: 'red' if x == max_value else 'pink')

st.header("Penyewaan Sepeda berdasarkan Musim (day.csv)")

plt.figure(figsize=(10, 6))
bars = plt.bar(season_counts['season'], season_counts['cnt'], color=season_counts['color'])
plt.title('Penyewaan Sepeda berdasarkan Musim (day.csv)')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan Sepeda')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')  # Va = vertical alignment

st.pyplot(plt)

# Regplot for temperature vs bike rentals
st.header("Hubungan Suhu dan Jumlah Penyewaan Sepeda (day.csv)")

plt.figure(figsize=(10, 6))
sns.regplot(x='temp', y='cnt', data=day_df, scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})
plt.title('Hubungan Suhu dan Jumlah Penyewaan Sepeda (day.csv)')
plt.xlabel('Suhu')
plt.ylabel('Jumlah Penyewaan Sepeda')

st.pyplot(plt)

# Line plot for hourly bike rentals
st.header("Pola Penyewaan Sepeda Berdasarkan Jam (hour.csv)")

plt.figure(figsize=(12, 6))
sns.lineplot(x='hr', y='cnt', data=hour_df, ci=None, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)
plt.title('Pola Penyewaan Sepeda Berdasarkan Jam (hour.csv)', fontsize=16, fontweight='bold')
plt.xlabel('Jam', fontsize=14)
plt.ylabel('Jumlah Penyewaan', fontsize=14)
plt.grid(True)

st.pyplot(plt)

# Bar plot for weather conditions and bike rentals
weather_counts = day_df.groupby('weathersit')['cnt'].sum().reset_index()
max_count = weather_counts['cnt'].max()

st.header("Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda (day.csv)")

plt.figure(figsize=(10, 6))
for index, row in weather_counts.iterrows():
    if row['cnt'] == max_count:
        plt.bar(row['weathersit'], row['cnt'], color='blue')  # Bar tertinggi
    else:
        plt.bar(row['weathersit'], row['cnt'], color='lightblue')  # Bar lainnya

plt.title('Pengaruh Kondisi Cuaca terhadap Penyewaan Sepeda (day.csv)', fontsize=16)
plt.xlabel('Kondisi Cuaca', fontsize=14)
plt.ylabel('Total Penyewaan Sepeda', fontsize=14)
plt.grid(axis='y')

st.pyplot(plt)
