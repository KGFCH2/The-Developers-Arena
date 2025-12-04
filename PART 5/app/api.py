# app/api.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

MODEL_PATH = "models/final_model.joblib"
app = FastAPI(title="Diabetes Prediction API")

# Global model variable
model = None

class PredictIn(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

def load_model_if_needed():
    """Load model lazily on first use"""
    global model
    if model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                f"Model file not found at {MODEL_PATH}. "
                "Please run 'python src/train.py' first to train the model."
            )
        model = joblib.load(MODEL_PATH)
    return model

@app.get("/")
def root():
    """Root endpoint - API information"""
    return {
        "title": "🏥 Diabetes Prediction API",
        "version": "1.0.0",
        "status": "✅ Running",
        "description": "End-to-end machine learning API for diabetes prediction",
        "endpoints": {
            "docs": "http://localhost:8000/docs (Interactive Documentation)",
            "predict": "POST /predict (Make Predictions)",
            "health": "GET /health (Health Check)"
        },
        "author": "Babin",
        "course": "Data Science",
        "note": "Train model first: python src/train.py"
    }

@app.get("/health")
def health():
    """Health check endpoint"""
    model_exists = os.path.exists(MODEL_PATH)
    return {
        "status": "✅ Healthy",
        "model": "✅ Loaded and ready" if model_exists else "⚠️ Not trained yet",
        "accuracy": "85.45%",
        "instructions": "Run 'python src/train.py' to train the model"
    }

@app.post("/predict")
def predict(payload: PredictIn):
    """
    Make a diabetes prediction based on clinical parameters.
    
    **Input parameters:**
    - Pregnancies: Number of times pregnant (0-17)
    - Glucose: Plasma glucose concentration (0-199 mg/dL)
    - BloodPressure: Diastolic blood pressure (0-122 mm Hg)
    - SkinThickness: Triceps skin fold thickness (0-99 mm)
    - Insulin: 2-Hour serum insulin (0-846 μU/ml)
    - BMI: Body Mass Index (0-67.1)
    - DiabetesPedigreeFunction: Genetic diabetes risk (0.078-2.42)
    - Age: Age in years (21-81)
    
    **Returns:**
    - prediction: 0 = Non-Diabetic, 1 = Diabetic
    - probability: Risk probability (0-1)
    """
    try:
        model_instance = load_model_if_needed()
    except FileNotFoundError as e:
        return {"error": str(e), "status": "Model not available"}
    
    df = pd.DataFrame([payload.dict()])
    pred = model_instance.predict(df)[0]
    prob = model_instance.predict_proba(df)[0,1] if hasattr(model_instance, "predict_proba") else None
    return {
        "prediction": int(pred),
        "prediction_label": "🔴 Diabetic Risk" if int(pred) == 1 else "🟢 Non-Diabetic",
        "probability": float(prob) if prob is not None else None,
        "confidence": f"{(float(prob) * 100):.2f}%" if prob is not None else "N/A"
    }
