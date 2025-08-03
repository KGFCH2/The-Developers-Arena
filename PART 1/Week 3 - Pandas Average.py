#  Clean and aggregate a dataset

import pandas as pd
import numpy as np

print("📊 Dataset Cleaner & Aggregator")

# Step 1: Create a sample dataset using user input
n = int(input("Enter number of rows: "))
data = []

for i in range(n):
    name = input(f"\nEnter name of person {i+1}: ")
    
    age_input = input("Enter age (leave blank if unknown): ")
    marks_input = input("Enter marks (leave blank if unknown): ")

    try:
        age = int(age_input) if age_input.strip() != "" else np.nan
    except ValueError:
        age = np.nan

    try:
        marks = float(marks_input) if marks_input.strip() != "" else np.nan
    except ValueError:
        marks = np.nan

    data.append({"Name": name, "Age": age, "Marks": marks})

# Step 2: Create DataFrame
df = pd.DataFrame(data)
print("\n📄 Original Dataset:\n", df)

# Step 3: Clean the dataset (remove rows with missing values)
clean_df = df.dropna()

# Step 4: Aggregate the data
average_age = clean_df["Age"].mean()
average_marks = clean_df["Marks"].mean()

# Step 5: Show results
print("\n🧹 Cleaned Dataset (no missing values):\n", clean_df)
print(f"\n📈 Average Age: {round(average_age, 2)}")
print(f"📈 Average Marks: {round(average_marks, 2)}")
