# src/data_prep.py
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split

TARGET = "Outcome"

MISSING_AS_ZERO = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

def load_data(path="data/raw/diabetes.csv"):
    df = pd.read_csv(path)
    return df

def clean_and_feature_engineer(df):
    df = df.copy()
    # Replace zeroes in certain columns with NaN (these zeros are missing values in this dataset)
    for col in MISSING_AS_ZERO:
        if col in df.columns:
            df.loc[df[col] == 0, col] = np.nan

    # Impute simple: we'll do median imputation in pipeline, but for EDA keep counts
    # Add a BMI age group as a simple engineered feature (example)
    if "BMI" in df.columns and "Age" in df.columns:
        df["BMI_age_ratio"] = df["BMI"] / (df["Age"] + 1e-6)

    # Ensure consistent dtypes
    return df

def split_save(df, out_dir="data/processed", test_size=0.2, random_state=42):
    os.makedirs(out_dir, exist_ok=True)
    # Drop rows with NaN in target variable
    df = df.dropna(subset=[TARGET])
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    train = pd.concat([X_train, y_train.reset_index(drop=True)], axis=1)
    test = pd.concat([X_test, y_test.reset_index(drop=True)], axis=1)
    train.to_csv(os.path.join(out_dir, "train.csv"), index=False)
    test.to_csv(os.path.join(out_dir, "test.csv"), index=False)
    print(f"Saved processed train/test to {out_dir}")
    return os.path.join(out_dir, "train.csv"), os.path.join(out_dir, "test.csv")

if __name__ == "__main__":
    df = load_data()
    df = clean_and_feature_engineer(df)
    split_save(df)
