# 🎯 Complete Instructions Manual

**Diabetes Prediction ML Project - Step-by-Step Guide**

---

## 🚀 Quick Start (Choose Your Path)

### Path 1: 👶 Beginner (Web App - Easiest!)
```bash
pip install -r requirements.txt
python src/data_prep.py
python src/train.py
python -m streamlit run app/streamlit_app.py
```
→ Browser opens at `http://localhost:8501` - Done! ✅

### Path 2: 💻 Developer (REST API)
```bash
pip install -r requirements.txt
python src/data_prep.py
python src/train.py
python -m uvicorn app.api:app --reload
```
→ API docs at `http://localhost:8000/docs` - Done! ✅

### Path 3: 🤖 Full ML Pipeline
```bash
pip install -r requirements.txt
python src/data_prep.py
python src/train.py
python src/evaluate.py
python src/predict.py models/final_model.joblib data/processed/test.csv
python src/visualize_results.py
```
→ All files in `models/` folder - Done! ✅

---

## 📖 Detailed Step-by-Step

### Step 1: Check Python Installation
```bash
python --version
# Should show Python 3.10 or higher
```

If not installed, download from https://www.python.org/downloads/

### Step 2: Navigate to Project Folder
```bash
cd path/to/PART 5
```

### Step 3: Create Virtual Environment (Optional)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🎯 What Each Program Does

### Data Processing
| Command | What It Does | Output |
|---------|--------------|--------|
| `python src/data_prep.py` | Cleans data, handles missing values, splits train/test | `data/processed/train.csv`, `test.csv` |

### Model Training
| Command | What It Does | Output |
|---------|--------------|--------|
| `python src/train.py` | Trains Random Forest model with GridSearchCV | `models/final_model.joblib` |

### Model Evaluation
| Command | What It Does | Output |
|---------|--------------|--------|
| `python src/evaluate.py` | Calculates accuracy, creates confusion matrix | `models/evaluation_report.png` |

### Batch Predictions
| Command | What It Does | Output |
|---------|--------------|--------|
| `python src/predict.py models/final_model.joblib data/processed/test.csv` | Predicts on CSV file | `data/processed/predictions.csv` |

### Visualizations
| Command | What It Does | Output |
|---------|--------------|--------|
| `python src/visualize_results.py` | Creates charts | 3 PNG files in `models/` |

---

## 🌐 Using Web Applications

### Streamlit Web App
```bash
python -m streamlit run app/streamlit_app.py
```

**Features:**
- Interactive input form
- Real-time predictions
- Risk gauge visualization
- Color-coded results

**To stop:** Press `Ctrl+C`

### REST API
```bash
python -m uvicorn app.api:app --reload
```

**Endpoints:**
- `GET /` - API info
- `GET /health` - Health check
- `POST /predict` - Make prediction

**Example API call:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Pregnancies": 2,
    "Glucose": 130,
    "BloodPressure": 80,
    "SkinThickness": 25,
    "Insulin": 100,
    "BMI": 28.5,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 45
  }'
```

**Response:**
```json
{
  "prediction": 0,
  "prediction_label": "🟢 Non-Diabetic",
  "probability": 0.2847,
  "confidence": "28.47%"
}
```

---

## 📊 Generated Files

After running the pipeline, check `models/` folder:

| File | Size | Description |
|------|------|-------------|
| `final_model.joblib` | 2.3 MB | Trained ML model |
| `evaluation_report.png` | 473 KB | 6-panel evaluation dashboard |
| `feature_importance.png` | 141 KB | Feature importance chart |
| `prediction_viz.png` | 134 KB | Prediction visualization |
| `data_distribution.png` | 438 KB | Data distribution analysis |

---

## 🔧 Common Problems & Solutions

### Problem: "Python command not found"
```bash
# Use python3 on Mac/Linux
python3 src/data_prep.py
```

### Problem: "No module named 'pandas'"
```bash
pip install -r requirements.txt
```

### Problem: "Model file not found"
```bash
python src/train.py
```

### Problem: "Port 8501 already in use"
```bash
python -m streamlit run app/streamlit_app.py --server.port 8502
```

### Problem: "Port 8000 already in use"
```bash
python -m uvicorn app.api:app --port 8001
```

### Problem: "Feature names mismatch in predict.py"
The script automatically handles this - just run:
```bash
python src/predict.py models/final_model.joblib data/processed/test.csv
```

---

## 💡 Quick Command Reference

### Setup
```bash
pip install -r requirements.txt
python -m venv venv
```

### Data Pipeline
```bash
python src/data_prep.py
python src/train.py
python src/evaluate.py
python src/visualize_results.py
```

### Run Apps
```bash
python -m streamlit run app/streamlit_app.py
python -m uvicorn app.api:app --reload
```

---

## ✅ Success Checklist

- [ ] Python 3.10+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Data prepared (`python src/data_prep.py`)
- [ ] Model trained (`python src/train.py`)
- [ ] Model evaluated (`python src/evaluate.py`)
- [ ] Visualizations created (`python src/visualize_results.py`)
- [ ] Streamlit app works (`http://localhost:8501`)
- [ ] API works (`http://localhost:8000/docs`)

**All checked? You're done! 🎉**

---

## 📚 Documentation Files

| File | Description |
|------|-------------|
| `README.md` | Project overview |
| `INSTRUCTIONS.md` | This file - detailed guide |
| `SETUP_GUIDE.md` | Troubleshooting & setup help |
| `report/Final_report.md` | Technical documentation |

---

<p align="center">
  <b>🎉 Enjoy your diabetes prediction system!</b><br>
  <i>Last Updated: December 5, 2025</i>
</p>
