# week7_ml.py
# Introduction to Machine Learning - Linear Regression example
# Usage: put dataset with numeric features and a target column 'target', then run: python week7_ml.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# === Embedded CSV Data ===
csv_data = """HouseID,Area,Bedrooms,Bathrooms,Stories,Parking,Price
1,2100,3,2,2,1,350000
2,1600,2,1,1,1,230000
3,2400,4,3,2,2,450000
4,3000,4,3,3,2,600000
5,1850,3,2,1,1,280000
6,1500,2,1,1,1,200000
7,2750,4,3,2,2,520000
8,2200,3,2,2,1,370000
9,1400,2,1,1,0,180000
10,2600,4,3,2,2,480000
11,1950,3,2,1,1,290000
12,3100,5,4,3,3,650000
13,1700,2,2,1,1,250000
14,2300,3,2,2,1,360000
15,2800,4,3,3,2,550000
"""

# Load dataset
df = pd.read_csv(StringIO(csv_data))

# === Basic Info ===
print("\n===== HEAD =====")
print(df.head())

print("\n===== INFO =====")
print(df.info())

print("\n===== DESCRIBE =====")
print(df.describe())

# === EDA ===
plt.figure(figsize=(6,4))
sns.histplot(df['Price'], kde=True, bins=6)
plt.title("House Price Distribution")
plt.show()

plt.figure(figsize=(6,4))
sns.scatterplot(x='Area', y='Price', data=df)
plt.title("Area vs Price")
plt.show()

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# === Train Model ===
X = df[['Area','Bedrooms','Bathrooms','Stories','Parking']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# === Predictions ===
y_pred = model.predict(X_test)

print("\n===== Model Evaluation =====")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred, squared=False))
print("R2 Score:", r2_score(y_test, y_pred))

# === Example Prediction ===
sample_house = [[2500, 3, 2, 2, 1]]  # Area=2500, 3BHK, 2Bath, 2Stories, 1Parking
predicted_price = model.predict(sample_house)[0]
print(f"\nPredicted Price for {sample_house}: ${predicted_price:,.2f}")
