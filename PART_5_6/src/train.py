# src/train.py
import pandas as pd
import joblib
import os
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

TARGET = "Outcome"

def load_train(path=None):
    if path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "../data/processed/train.csv")
    return pd.read_csv(path)

def build_pipeline(model):
    numeric_imputer = SimpleImputer(strategy="median")
    scaler = StandardScaler()
    pipeline = Pipeline([
        ("imputer", numeric_imputer),
        ("scaler", scaler),
        ("model", model)
    ])
    return pipeline

def train_and_save(task_model="random_forest"):
    df = load_train()
    # Drop rows with any NaN values
    # df = df.dropna()  <-- REMOVED: Let the pipeline imputer handle missing values
    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    print(f"Original class distribution: {y.value_counts().to_dict()}")
    print(f"Class imbalance ratio: {y.value_counts()[0] / y.value_counts()[1]:.2f}:1")

    if task_model == "logistic":
        base = LogisticRegression(max_iter=1000, random_state=42)
        param_grid = {
            "model__C": [0.01, 0.1, 1.0, 10.0]
        }
    else:
        # Calculate custom class weights to give much more emphasis to minority class
        class_weights = {0: 1, 1: 10}  # Give 10x weight to diabetic class
        base = RandomForestClassifier(random_state=42, n_jobs=-1, class_weight=class_weights)
        param_grid = {
            "model__n_estimators": [100, 200],
            "model__max_depth": [10, 15, 20],
            "model__min_samples_split": [5, 10]
        }

    pipe = build_pipeline(base)
    gs = GridSearchCV(pipe, param_grid, cv=5, scoring="roc_auc", n_jobs=-1, verbose=2)
    gs.fit(X, y)
    print("Best params:", gs.best_params_)
    best = gs.best_estimator_

    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_dir = os.path.join(base_dir, "../models")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "final_model.joblib")
    joblib.dump(best, model_path)
    print(f"Saved model to {model_path}")
    return gs

if __name__ == "__main__":
    train_and_save()
