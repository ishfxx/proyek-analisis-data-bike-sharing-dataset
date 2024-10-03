import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cache the data loading function to optimize performance
@st.cache
def load_data():
    # Adjust the path to the datasets as needed
    day_df = pd.read_csv('data/day.csv')
    hour_df = pd.read_csv('data/hour.csv')
    return day_df, hour_df

# Business Questions
st.title("Bike Sharing Data Analysis")
st.markdown("""
## Business Questions:
- **Which season has the highest bike rentals?**
- **How does temperature affect daily bike rentals?**
- **How does temperature affect bike rentals at specific hours?**
- **How does weather condition affect total bike rentals?**
""")

# Load the datasets
day_df, hour_df = load_data()

# Checking missing values
st.header("Checking missing values for 'day.csv':")
st.write(day_df.isnull().sum())

st.header("Checking missing values for 'hour.csv':")
st.write(hour_df.isnull().sum())

# Data types and summary
st.header("Data types and summary for 'day.csv':")
st.write(day_df.dtypes)
st.write(day_df.describe())

st.header("Data types and summary for 'hour.csv':")
st.write(hour_df.dtypes)
st.write(hour_df.describe())

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

# Analysis of Rentals by Season (addressing the first business question)
season_counts = day_df.groupby('season')['cnt'].sum().reset_index()
max_value = season_counts['cnt'].max()
season_counts['color'] = season_counts['cnt'].apply(lambda x: 'red' if x == max_value else 'pink')

st.header("Season-wise Total Bike Rentals (day.csv)")
plt.figure(figsize=(8, 5))
plt.bar(season_counts['season'], season_counts['cnt'], color=season_counts['color'])
plt.title('Total Bike Rentals by Season', fontsize=16)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Total Rentals', fontsize=14)
st.pyplot(plt)
plt.close()

# Select numerical columns for correlation matrix
numerical_cols_day = day_df.select_dtypes(include=['float64', 'int64'])
numerical_cols_hour = hour_df.select_dtypes(include=(['float64', 'int64']))

# Plot correlation matrices (addressing temperature and rental correlation)
st.header("Correlation Matrices")

fig, axes = plt.subplots(2, 1, figsize=(10, 12))
sns.heatmap(numerical_cols_day.corr(), annot=True, cmap='coolwarm', ax=axes[0])
axes[0].set_title('Correlation Matrix - day.csv')

sns.heatmap(numerical_cols_hour.corr(), annot=True, cmap='coolwarm', ax=axes[1])
axes[1].set_title('Correlation Matrix - hour.csv')

st.pyplot(fig)
plt.close()

# Hourly rentals (addressing how temperature affects rentals at specific hours)
hourly_rentals = hour_df.groupby('hr')['cnt'].mean().reset_index()
max_rentals = hourly_rentals['cnt'].max()

st.header("Average Hourly Bike Rentals (hour.csv)")
plt.figure(figsize=(10, 6))
plt.bar(hourly_rentals['hr'], hourly_rentals['cnt'], color='orange')
plt.title('Average Hourly Bike Rentals', fontsize=16)
plt.xlabel('Hour', fontsize=14)
plt.ylabel('Average Rentals', fontsize=14)
plt.grid(True)

st.pyplot(plt)
plt.close()

# Bar plot for weather conditions and bike rentals (addressing the effect of weather on rentals)
weather_counts = day_df.groupby('weathersit')['cnt'].sum().reset_index()
max_count = weather_counts['cnt'].max()

st.header("Impact of Weather Conditions on Bike Rentals (day.csv)")
plt.figure(figsize=(10, 6))
for index, row in weather_counts.iterrows():
    if row['cnt'] == max_count:
        plt.bar(row['weathersit'], row['cnt'], color='blue')
    else:
        plt.bar(row['weathersit'], row['cnt'], color='lightblue')

plt.title('Impact of Weather on Bike Rentals', fontsize=16)
plt.xlabel('Weather Condition', fontsize=14)
plt.ylabel('Total Rentals', fontsize=14)
plt.grid(axis='y')

st.pyplot(plt)
plt.close()
