
# Step 1: Load Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("Set2")

# Step 2: Load the CSV file
df = pd.read_csv("results.csv")

# Display first few rows
print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)
print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nDataset Statistics:")
print(df.describe())