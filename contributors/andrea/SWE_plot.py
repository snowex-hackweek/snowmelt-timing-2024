# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

# Load the CSV file
df = pd.read_csv('SP_20_NM.csv')

# Print out the column names
print(df.head())

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the CSV file
df = pd.read_csv('SP_20_NM.csv', skiprows=32)

# Ignore the first 31 rows
df = df.drop(axis=0, index=0)

# Convert the 'time' column to datetime format with the specified format
df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%dT%H:%M', errors='coerce')

# Replace -9999 with NaN in the 'SWE' column
df['SWE (mm)'] = df['SWE (mm)'].replace(-9999, np.nan)

# Set plot style
sns.set(style="whitegrid")

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot data for each site separately
for site in df['Site'].unique():
    subset = df[df['Site'] == site]
    plt.plot(subset['time'], subset['SWE (mm)'], marker='o', label=site)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('SWE (mm)')
plt.title('SWE over Time for Different Research Sites in NM')
plt.legend()

# Display the plot
plt.show()

# %%
print(df['time'])

# %%
print(df.columns)

# %%
