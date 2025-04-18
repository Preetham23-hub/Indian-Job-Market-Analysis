# -*- coding: utf-8 -*-
"""Job-market-analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y4W4pVkwWtp_XyPL4lp5JgR5_fmxVhDz
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

"""API Configuration"""

# API endpoint and your API key
API_URL = "https://jobs.indianapi.in/jobs"
API_KEY = "<API-KEY>"  # Replace with your actual API key

# Parameters for the API request
params = {
    "location": "Bangalore",
    "title": "Software Engineer",
    "experience": "Mid-Level",
    "limit": "100"  # Adjust limit as needed
}

# Headers for the API request
headers = {
    "X-Api-Key": API_KEY
}

"""Data Fetching Function"""

# Function to fetch data from the API
def fetch_job_data(url, headers, params):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

"""Fetch and Check Data"""

# Fetch job data
job_data = fetch_job_data(API_URL, headers, params)

# Check if data was fetched successfully
if job_data:
    print("Data fetched successfully!")
    print(f"Total records: {len(job_data)}")
    print(job_data[:10])  # Raw first 10 records (exact API output)
else:
    print("Failed to retrieve job data.")

"""Data Processing"""

# Convert to DataFrame and parse dates
df = pd.DataFrame(job_data)
df['posted_date'] = pd.to_datetime(df['posted_date'], errors='coerce')

# Extract year/month and filter for 2025
df['year'] = df['posted_date'].dt.year
df['month'] = df['posted_date'].dt.month
df_2025 = df[df['year'] == 2025]

# Group by month (force all 12 months)
monthly_postings = (
    df_2025['month'].value_counts()
    .sort_index()
    .reindex(range(1,13), fill_value=0)  # Ensure 12 months
)

print("2025 Data Summary:")
print(f"- Total records: {len(df_2025)}")
print(f"- Months with data: {df_2025['month'].unique()}")
print("\nMonthly Counts:\n", monthly_postings)

"""
Display Processed Data

"""

# 1. Show processed DataFrame sample
print("Processed DataFrame Sample (First 5 Rows):")
display(df.head())  # Interactive table in Colab

# 2. Show filtered 2025 data stats
print(f"\n 2025 Records: {len(df_2025)} ({(len(df_2025)/len(df))*100:.1f}% of total)")

# 3. Monthly counts as a table
print("\n Monthly Postings (2025):")
print(monthly_postings.to_markdown(tablefmt="grid"))  # Pretty table

"""Data Visualization"""

plt.figure(figsize=(13, 7))

# 1. Color Settings - 12 unique colors (one per month)
colormap = plt.cm.get_cmap('tab20', 12)  # Options: 'tab20', 'rainbow', 'hsv', 'viridis'
colors = [colormap(i) for i in range(12)]  # Generate 12 distinct colors

# 2. Plot Bars with Custom Colors
bars = plt.bar(
    monthly_postings.index,
    monthly_postings.values,
    color=colors,
    edgecolor='white',
    linewidth=1.5,
    alpha=0.85
)

# 3. Value Labels (with dynamic positioning)
max_height = monthly_postings.max()
for bar in bars:
    height = bar.get_height()
    vertical_offset = max_height * 0.02  # 2% of max height as padding
    plt.text(
        bar.get_x() + bar.get_width()/2.,
        height + vertical_offset,
        f'{int(height)}',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold',
        color='black'
    )

# 4. Title & Axis Styling
plt.title(
    "Monthly Software Engineer Job Postings (Bangalore, 2025)",
    fontsize=15,
    fontweight='bold',
    pad=20,
    color='#2c3e50'
)

plt.xlabel(
    "Month",
    fontsize=12,
    labelpad=12,
    color='#2c3e50'
)
plt.ylabel(
    "Number of Postings",
    fontsize=12,
    labelpad=12,
    color='#2c3e50'
)

# 5. X-Axis Month Labels
plt.xticks(
    range(1, 13),
    ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
     'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
    rotation=45,
    fontsize=11,
    color='#34495e'
)

# 6. Grid & Frame Styling
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle=':', alpha=0.4)
for spine in ['top', 'right']:
    plt.gca().spines[spine].set_visible(False)

# 7. Footer Note
plt.figtext(
    0.5, -0.05,
    "Data Source: Indian API | Visualization by Your Name",
    ha="center",
    fontsize=9,
    color='#7f8c8d'
)

plt.tight_layout()
plt.show()