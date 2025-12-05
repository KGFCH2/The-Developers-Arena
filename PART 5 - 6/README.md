# 🏥 Diabetes Prediction ML Project

> **Predict diabetes risk instantly using Machine Learning**

| Metric | Value |
|--------|-------|
| **Accuracy** | 85.45% |
| **Algorithm** | Random Forest |
| **Status** | ✅ Ready to Use |

---

## ⚡ Quick Start

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Prepare data
python src/data_prep.py

# Step 3: Train the model
python src/train.py

# Step 4: Launch web app
python -m streamlit run app/streamlit_app.py
```

🎉 **Open http://localhost:8501** - Enter patient data and get predictions!

---

## 🚀 Two Ways to Use

### 1️⃣ Streamlit Web App (Easiest!)
```bash
python -m streamlit run app/streamlit_app.py
```
→ Opens at **http://localhost:8501**

### 2️⃣ REST API
```bash
python -m uvicorn app.api:app --reload
```
→ API Docs at **http://localhost:8000/docs**

---

## 📁 Project Structure

```
PART 5/
├── src/                      ← Python Scripts
│   ├── data_prep.py          → Prepare & clean data
│   ├── train.py              → Train ML model
│   ├── evaluate.py           → Evaluate model
│   ├── predict.py            → Batch predictions
│   └── visualize_results.py  → Generate charts
│
├── app/                      ← Web Applications
│   ├── api.py                → FastAPI backend
│   └── streamlit_app.py      → Interactive web UI
│
├── portfolio/                ← Frontend Website
│   ├── index.html            → Main showcase page
│   └── style.css             → Styling
│
├── data/                     ← Data Files
│   ├── raw/diabetes.csv      → Original dataset
│   └── processed/            → Train/test splits
│
├── models/                   ← Trained Model & Charts
│   ├── final_model.joblib    → Trained model
│   └── *.png                 → Evaluation visualizations
│
└── Documentation
    ├── README.md             → Project overview
    ├── INSTRUCTIONS.md       → Detailed guide
    └── SETUP_GUIDE.md        → Troubleshooting
```

---

## 📋 Run All Programs

| Step | Command | Output | Time |
|------|---------|--------|------|
| 1 | `python src/data_prep.py` | train.csv, test.csv | 2s |
| 2 | `python src/train.py` | final_model.joblib | 30s |
| 3 | `python src/evaluate.py` | evaluation_report.png | 5s |
| 4 | `python src/visualize_results.py` | 3 PNG charts | 5s |
| 5 | `python src/predict.py models/final_model.joblib data/processed/test.csv` | predictions.csv | 2s |

---

## 🔧 Input Features

| Feature | Description | Range |
|---------|-------------|-------|
| Pregnancies | Number of pregnancies | 0-17 |
| Glucose | Blood glucose (mg/dL) | 0-199 |
| BloodPressure | Blood pressure (mm Hg) | 0-122 |
| SkinThickness | Skin fold thickness (mm) | 0-99 |
| Insulin | Insulin level (μU/ml) | 0-846 |
| BMI | Body Mass Index | 0-67 |
| DiabetesPedigreeFunction | Family history score | 0.08-2.42 |
| Age | Age in years | 21-81 |

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `Model file not found` | `python src/train.py` |
| Port 8501 in use | `--server.port 8502` |
| Port 8000 in use | `--port 8001` |

---

## ✅ Verified Working

| Component | Status |
|-----------|--------|
| Data Preparation | ✅ Working |
| Model Training | ✅ 85.45% Accuracy |
| Model Evaluation | ✅ Working |
| Batch Predictions | ✅ Working |
| Visualizations | ✅ 4 PNG files generated |
| Streamlit App | ✅ Working |
| FastAPI Backend | ✅ Working |
| Portfolio Website | ✅ Working |

---

## 👤 Author

**Babin Bid**  
📧 babinbid05@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/babin-bid-853728293/) | [GitHub](https://github.com/KGFCH2)

---

<p align="center">
  <b>✅ ML Application Ready!</b><br>
  <i>Last Updated: December 5, 2025</i>
</p>
