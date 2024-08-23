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
df = pd.read_csv('LWC_SP_200220.csv', skiprows=12)

# Print out the column names
print(df.head())

# %%
import numpy as np

# Use column indices to select relevant columns
LWCvolA = df.columns[5]  
LWCvolB = df.columns[6]  

# Create a new column 'Mean_Column1_Column2' that contains the mean of the two existing columns
df['LWC-volmean'] = df[[LWCvolA, LWCvolB]].mean(axis=1)

# print head
print(df[[LWCvolA, LWCvolB, 'LWC-volmean']].head())

# %%
df['LWCsum'] = df['LWC-volmean'].sum()
df['HS'] = df['# Top (cm)'].iloc[0]
df['LWCbulk'] = df['LWCsum'] / df ['HS']

print(df[['LWCsum', 'LWCbulk', 'HS']].head())

# %%
