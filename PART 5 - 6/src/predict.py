# src/predict.py
import joblib
import pandas as pd
import sys
import os

def predict_csv(model_path, input_csv, out_csv=None):
    if out_csv is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        out_csv = os.path.join(base_dir, "../data/processed/predictions.csv")
        
    model = joblib.load(model_path)
    df = pd.read_csv(input_csv)
    
    # If the input CSV has the target column (e.g. test.csv), drop it
    if "Outcome" in df.columns:
        df = df.drop(columns=["Outcome"])
        
    preds = model.predict(df)
    probs = model.predict_proba(df)[:,1] if hasattr(model, "predict_proba") else None
    df["prediction"] = preds
    if probs is not None:
        df["probability"] = probs
    df.to_csv(out_csv, index=False)
    print("Saved predictions to", out_csv)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python src/predict.py ../models/final_model.joblib ../data/processed/some_input.csv")
    else:
        predict_csv(sys.argv[1], sys.argv[2])
