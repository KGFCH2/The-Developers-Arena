# week5_eda.py
# Exploratory Data Analysis (EDA) example script
# Usage: place your dataset as 'data.csv' in the same folder and run: python week5_eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# === Embedded CSV Data ===
csv_data = """CustomerID,Age,Gender,Annual_Income,Spending_Score,Region
1,25,Male,40000,60,North
2,32,Female,52000,75,South
3,45,Male,61000,40,East
4,29,Female,58000,82,West
5,51,Male,72000,30,North
6,23,Female,35000,68,South
7,34,Male,45000,55,West
8,42,Female,64000,47,East
9,36,Male,50000,70,North
10,28,Female,39000,80,West
11,40,Male,55000,65,East
12,31,Female,47000,72,South
13,48,Male,73000,38,North
14,26,Female,36000,77,West
15,39,Male,60000,58,South
"""

# Load dataset from CSV string
df = pd.read_csv(StringIO(csv_data))

# === Basic Info ===
print("\n===== HEAD =====")
print(df.head())

print("\n===== INFO =====")
print(df.info())

print("\n===== DESCRIBE =====")
print(df.describe())

# === Missing Values ===
print("\n===== Missing Values =====")
print(df.isnull().sum())

# === Univariate Analysis ===
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], kde=True, bins=8)
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution")
plt.show()

# === Bivariate Analysis ===
plt.figure(figsize=(6,4))
sns.scatterplot(x='Annual_Income', y='Spending_Score', hue='Gender', data=df, s=80)
plt.title("Income vs Spending Score")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x='Region', y='Annual_Income', data=df)
plt.title("Income Distribution by Region")
plt.show()

# === Correlation Heatmap ===
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
