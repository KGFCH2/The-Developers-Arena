# 🏥 Diabetes Prediction & Analysis System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

> Predict diabetes risk using Advanced Machine Learning!

---

## 🏆 Project Highlights

| Metric | Value |
|:---:|:---:|
| Accuracy | 85.45% 🎯 |
| Algorithm | Random Forest 🌲 |
| Status | Ready to Use ✅ |
| Deployment | Streamlit & FastAPI 🌐 |

---

## ⚡ Quick Start Guide

Get up and running in seconds!

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Prepare & Clean Data
python src/data_prep.py

# Step 3: Train the AI Model
python src/train.py

# Step 4: Launch the Web App
python -m streamlit run app/streamlit_app.py
```

Open http://localhost:8501 - Enter patient data and get instant AI predictions! 🤖

---

## 🎮 Two Ways to Use

### 1. 🌟 Streamlit Web App (Visual & Easy!)
The most user-friendly way to interact with the model.
```bash
python -m streamlit run app/streamlit_app.py
```
Opens at: `http://localhost:8501`

### 2. ⚡ REST API (For Developers)
High-performance API backend using FastAPI.
```bash
python -m uvicorn app.api:app --reload
```
Docs at: `http://localhost:8000/docs`

---

## 📂 Project Architecture

```
PART_5_6/
├── src/                   # 🐍 Python Scripts
│   ├── data_prep.py       # 🧹 Data Cleaning
│   ├── train.py           # 🧠 Model Training
│   ├── evaluate.py        # 📊 Performance Report
│   ├── predict.py         # 🔮 Batch Predictions
│   └── visualize_results.py # 📈 Charts
│
├── app/                   # 🌐 Web Apps
│   ├── api.py             # ⚡ FastAPI Backend
│   └── streamlit_app.py   # 🌟 Streamlit Frontend
│
├── portfolio/             # 🎨 Showcase
│   ├── index.html         # 🏠 Main Portfolio Page
│   └── style.css          # 💅 Styling
│
├── data/                  # 💾 Data
│   ├── raw/diabetes.csv   # 📄 Raw Data
│   └── processed/         # ⚙️ Ready-to-train Data
│
├── models/                # 🤖 Intelligence
│   ├── final_model.joblib # 📦 Saved Model
│   └── *.png              # 🖼️ Visual Insights
│
└── Documentation
    ├── README.md          # 📖 You are here!
    ├── INSTRUCTIONS.md    # 🗺️ Detailed Map
    └── SETUP_GUIDE.md     # 🛠️ Fix-it Guide
```

---

## 🏃 Run All Programs

| Step | Command | Output | Time |
|:---:|---|---|:---:|
| 1 | `python src/data_prep.py` | `train.csv`, `test.csv` | 2s ⚡ |
| 2 | `python src/train.py` | `final_model.joblib` | 30s ⏳ |
| 3 | `python src/evaluate.py` | `evaluation_report.png` | 5s ⚡ |
| 4 | `python src/visualize_results.py` | 3x PNG Charts 📊 | 5s ⚡ |
| 5 | `python src/predict.py ...` | `predictions.csv` 🔮 | 2s ⚡ |

---

## 🧬 Input Features

| Feature | Description | Range |
|---|---|---|
| Pregnancies | Number of pregnancies | 0-17 |
| Glucose | Blood glucose (mg/dL) | 0-199 |
| BloodPressure | Blood pressure (mm Hg) | 0-122 |
| SkinThickness | Skin fold thickness (mm) | 0-99 |
| Insulin | Insulin level (μU/ml) | 0-846 |
| BMI | Body Mass Index | 0-67 |
| DiabetesPedigree | Family history score | 0.08-2.42 |
| Age | Age in years | 21-81 |

---

## ❓ Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError` | `pip install -r requirements.txt` 📦 |
| `Model file not found` | `python src/train.py` 🧠 |
| Port 8501 in use | `--server.port 8502` 🔌 |
| Port 8000 in use | `--port 8001` 🔌 |

---

## ✅ Verified Working Components

| Component | Status |
|---|---|
| Data Preparation | ✅ Working |
| Model Training | ✅ 85.45% Accuracy |
| Model Evaluation | ✅ Working |
| Batch Predictions | ✅ Working |
| Visualizations | ✅ 4 PNGs Generated |
| Streamlit App | ✅ Working |
| FastAPI Backend | ✅ Working |
| Portfolio Website | ✅ Working |

---

## 👨🏼‍💻 Author

**Babin Bid**  
📧 babinbid05@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/babin-bid-853728293/) | [GitHub](https://github.com/KGFCH2)

---

<p align="center">
  <b>Made with ❤️ by Babin Bid</b><br>
  <i>Last Updated: December 2025</i>
</p>
