# 🚀 Complete Setup & User Guide for Diabetes Prediction Project

**For Complete Beginners - Follow These Steps Exactly!**

---

## Table of Contents
1. [System Requirements](#system-requirements)
2. [Pre-Setup Checklist](#pre-setup-checklist)
3. [Step-by-Step Installation](#step-by-step-installation)
4. [Running the Complete Pipeline](#running-the-complete-pipeline)
5. [Using the Web Applications](#using-the-web-applications)
6. [API Testing Guide](#api-testing-guide)
7. [Troubleshooting](#troubleshooting)
8. [Common Issues & Solutions](#common-issues--solutions)

---

## System Requirements

### Minimum Requirements
- ✅ **Operating System:** Windows, macOS, or Linux
- ✅ **Python Version:** 3.10 or higher
- ✅ **RAM:** 4 GB minimum (8 GB recommended)
- ✅ **Disk Space:** 500 MB free
- ✅ **Internet:** Required for initial setup

### Check Your System

**On Windows (PowerShell):**
```powershell
python --version
```

**On macOS/Linux (Terminal):**
```bash
python3 --version
```

---

## Pre-Setup Checklist

Before starting, verify:

- [ ] Python is installed (version 3.10+)
- [ ] You have Git installed (optional but recommended)
- [ ] You have administrator access (for pip installations)
- [ ] Your internet connection is stable
- [ ] You have at least 500 MB free disk space

---

## Step-by-Step Installation

### Step 1️⃣: Download/Clone the Project

**Option A: Using Git (Recommended)**
```bash
git clone https://github.com/KGFCH2/The-Developers-Arena.git
cd "The-Developers-Arena/PART 5"
```

**Option B: Manual Download**
1. Download the project ZIP file
2. Extract it to your desired location
3. Open terminal/PowerShell in the extracted folder

### Step 2️⃣: Create a Virtual Environment (Optional but Recommended)

Virtual environments isolate project dependencies from your system Python.

**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On macOS/Linux (Terminal):**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt if successful.

### Step 3️⃣: Install Dependencies

Copy and paste this command to install all required packages:

```bash
pip install -r requirements.txt
```

**What this installs:**
- pandas, numpy (Data processing)
- scikit-learn (Machine learning)
- matplotlib, seaborn (Visualizations)
- fastapi, uvicorn (API server)
- streamlit (Web interface)
- joblib (Model serialization)

⏳ This takes 2-5 minutes depending on internet speed.

**Expected Output:**
```
Successfully installed pandas numpy scikit-learn matplotlib streamlit fastapi uvicorn ...
```

---

## Running the Complete Pipeline

### Full ML Pipeline (All Steps in Order)

Run these commands in sequence to generate everything:

#### Command 1: Prepare Data
```powershell
# Windows PowerShell
&"C:/Program Files/Python313/python.exe" src/data_prep.py
```

```bash
# macOS/Linux
python3 src/data_prep.py
```

**What it does:**
- ✅ Loads raw dataset (2,500 samples)
- ✅ Cleans missing values (NaN handling)
- ✅ Splits into train (80%) and test (20%)
- ✅ Saves: `data/processed/train.csv` and `test.csv`

**Expected Output:**
```
Saved processed train/test to data/processed
```

---

#### Command 2: Train Model
```powershell
# Windows PowerShell
&"C:/Program Files/Python313/python.exe" src/train.py
```

```bash
# macOS/Linux
python3 src/train.py
```

**What it does:**
- ✅ Loads prepared training data
- ✅ Tests 2 models: Logistic Regression & Random Forest
- ✅ Optimizes hyperparameters using GridSearchCV
- ✅ Trains best model (Random Forest)
- ✅ Saves: `models/final_model.joblib` (2.3 MB)

**Expected Output:**
```
Best params: {'model__n_estimators': 100, 'model__max_depth': None}
Saved model to models/final_model.joblib
```

---

#### Command 3: Evaluate Model
```powershell
# Windows PowerShell
&"C:/Program Files/Python313/python.exe" src/evaluate.py
```

```bash
# macOS/Linux
python3 src/evaluate.py
```

**What it does:**
- ✅ Tests model on test dataset
- ✅ Calculates metrics (Accuracy: 85.45%)
- ✅ Generates 6-panel visualization dashboard
- ✅ Saves: `models/evaluation_report.png` (473 KB, 300 DPI)

**Expected Output:**
```
==================================================
MODEL EVALUATION RESULTS
==================================================
Accuracy: 0.8545
ROC AUC: 0.4800
Classification report: ...
==================================================
✅ Evaluation report saved to: models/evaluation_report.png
```

---

#### Command 4: Generate Additional Visualizations
```powershell
# Windows PowerShell
&"C:/Program Files/Python313/python.exe" src/visualize_results.py
```

```bash
# macOS/Linux
python3 src/visualize_results.py
```

**What it does:**
- ✅ Creates feature importance chart
- ✅ Creates prediction visualizations
- ✅ Creates data distribution analysis
- ✅ Saves 3 PNG files (300 DPI)

**Expected Output:**
```
✅ Feature importance visualization saved to: models/feature_importance.png
✅ Prediction visualization saved to: models/prediction_viz.png
✅ Data distribution visualization saved to: models/data_distribution.png
```

---

### Quick Test (If Data/Model Already Exist)

If you already have `final_model.joblib` and processed data:

```powershell
# Just evaluate
&"C:/Program Files/Python313/python.exe" src/evaluate.py
```

---

## Using the Web Applications

### Option A: 🌐 Interactive Web App (Streamlit)

**Easiest for Beginners!**

#### Run Streamlit App:
```powershell
# Windows PowerShell
&"C:/Program Files/Python313/python.exe" -m streamlit run app/streamlit_app.py
```

```bash
# macOS/Linux
python3 -m streamlit run app/streamlit_app.py
```

**Expected Output:**
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

#### Using the App:
1. **Open Browser:** Go to `http://localhost:8501`
2. **Enter Patient Data:** Fill in the clinical parameters
3. **Click Predict Button:** 🔮 "Predict"
4. **View Results:** See prediction with probability and visualizations
5. **See Patient Profile:** Review all entered values in a table

**Features:**
- ✅ Interactive sliders and number inputs
- ✅ Real-time prediction
- ✅ Visualization of prediction confidence
- ✅ Risk gauge display
- ✅ Patient profile summary

**To Stop:**
- Press `Ctrl+C` in the terminal
- Or close the browser tab

---

### Option B: 🔌 REST API (FastAPI)

**For developers and programmatic access**

#### Run API Server:
```powershell
# Windows PowerShell
&"C:/Program Files/Python313/python.exe" -m uvicorn app.api:app --reload
```

```bash
# macOS/Linux
python3 -m uvicorn app.api:app --reload
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process
INFO:     Started server process
```

#### API Endpoints:

**1. Interactive Documentation (Visit in Browser):**
```
http://localhost:8000/docs
```
- Full API documentation
- Try endpoints directly
- See request/response examples

**2. Root Endpoint (Check API Status):**
```
http://localhost:8000/
```
Returns:
```json
{
  "title": "🏥 Diabetes Prediction API",
  "status": "✅ Running",
  "endpoints": {...}
}
```

**3. Health Check:**
```
http://localhost:8000/health
```
Returns:
```json
{
  "status": "✅ Healthy",
  "model": "Loaded and ready",
  "accuracy": "85.45%"
}
```

**4. Make Prediction:**
```
POST http://localhost:8000/predict
```

**Example Request (using curl):**
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

**Example Response:**
```json
{
  "prediction": 0,
  "prediction_label": "🟢 Non-Diabetic",
  "probability": 0.2847,
  "confidence": "28.47%"
}
```

---

## API Testing Guide

### Using Python Requests

```python
import requests
import json

# API URL
API_URL = "http://localhost:8000/predict"

# Patient data
patient = {
    "Pregnancies": 2,
    "Glucose": 130,
    "BloodPressure": 80,
    "SkinThickness": 25,
    "Insulin": 100,
    "BMI": 28.5,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 45
}

# Make prediction
response = requests.post(API_URL, json=patient)
result = response.json()

print(json.dumps(result, indent=2))
```

### Using Postman

1. Download [Postman](https://www.postman.com/downloads/)
2. Create new POST request
3. URL: `http://localhost:8000/predict`
4. Headers: `Content-Type: application/json`
5. Body (raw JSON):
```json
{
  "Pregnancies": 2,
  "Glucose": 130,
  "BloodPressure": 80,
  "SkinThickness": 25,
  "Insulin": 100,
  "BMI": 28.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 45
}
```
6. Click "Send"

---

## Troubleshooting

### Issue 1: Python Not Found

**Error:**
```
'python' is not recognized as an internal or external command
```

**Solution:**
```powershell
# Try python3 instead
python3 src/data_prep.py

# Or use full path
"C:/Program Files/Python313/python.exe" src/data_prep.py

# Or check if in venv
.\venv\Scripts\Activate.ps1
```

---

### Issue 2: Package Not Installed

**Error:**
```
ModuleNotFoundError: No module named 'pandas'
```

**Solution:**
```bash
# Reinstall all packages
pip install -r requirements.txt

# Or install specific package
pip install pandas scikit-learn
```

---

### Issue 3: Model File Not Found

**Error:**
```
FileNotFoundError: models/final_model.joblib not found
```

**Solution:**
```bash
# Run training first
python src/train.py

# Or download pre-trained model from GitHub
```

---

### Issue 4: Port Already in Use

**Error (Streamlit):**
```
ERROR: Port 8501 already in use
```

**Solution:**
```powershell
# Use different port
python -m streamlit run app/streamlit_app.py --server.port 8502
```

**Error (API):**
```
ERROR: Address already in use
```

**Solution:**
```bash
# Use different port
uvicorn app.api:app --port 8001
```

---

### Issue 5: Virtual Environment Issues

**Error:**
```
The term 'Activate.ps1' is not recognized
```

**Solution:**
```powershell
# Create new venv
python -m venv venv

# Set execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Activate
.\venv\Scripts\Activate.ps1
```

---

## Common Issues & Solutions

### ❓ Q: How do I know if everything is installed correctly?

**A:** Run this diagnostic:
```bash
python -c "import pandas, numpy, sklearn, streamlit, fastapi; print('✅ All packages installed!')"
```

---

### ❓ Q: Can I run both Streamlit and API at the same time?

**A:** Yes! Open two terminal windows:
- **Terminal 1:** `python -m streamlit run app/streamlit_app.py`
- **Terminal 2:** `python -m uvicorn app.api:app --reload`

---

### ❓ Q: What if I see a model accuracy of 0% or strange results?

**A:** Your model file might be corrupted. Retrain:
```bash
python src/train.py
```

---

### ❓ Q: How do I view the generated visualizations?

**A:** Navigate to `models/` folder and open PNG files:
- `evaluation_report.png` - Main dashboard
- `feature_importance.png` - Feature ranking
- `prediction_viz.png` - Prediction charts
- `data_distribution.png` - Data analysis

---

### ❓ Q: Can I use this on macOS/Linux?

**A:** Yes! Use `python3` instead of `python`:
```bash
python3 src/data_prep.py
python3 src/train.py
python3 src/evaluate.py
python3 -m streamlit run app/streamlit_app.py
python3 -m uvicorn app.api:app --reload
```

---

### ❓ Q: How do I deactivate the virtual environment?

**A:**
```bash
# Either terminal:
deactivate

# Or PowerShell:
.\venv\Scripts\Deactivate.ps1
```

---

## Quick Reference Command Cheat Sheet

```bash
# SETUP
python -m venv venv              # Create virtual environment
.\venv\Scripts\Activate.ps1      # Activate (Windows)
source venv/bin/activate         # Activate (macOS/Linux)
pip install -r requirements.txt  # Install packages

# PIPELINE
python src/data_prep.py          # Prepare data
python src/train.py              # Train model
python src/evaluate.py           # Evaluate & visualize
python src/visualize_results.py  # Generate visualizations

# RUNNING APPS
python -m streamlit run app/streamlit_app.py
python -m uvicorn app.api:app --reload

# DEACTIVATE
deactivate                        # Exit virtual environment
```

---

## Next Steps

1. ✅ **Complete Installation** → Run all setup steps
2. ✅ **Run Full Pipeline** → Generate model and visualizations
3. ✅ **Test Streamlit App** → Make predictions interactively
4. ✅ **Test API** → Verify endpoints work
5. ✅ **View Portfolio** → Open `portfolio/index.html` in browser
6. ✅ **Read Documentation** → Check `report/Final_report.md`

---

## Support & Resources

- 📖 **Full Documentation:** See `README.md`
- 📊 **Technical Report:** See `report/Final_report.md`
- 🎨 **Portfolio:** Open `portfolio/index.html`
- 💻 **GitHub:** https://github.com/KGFCH2/The-Developers-Arena
- ❓ **Issues:** Check common issues above

---

**🎉 Congratulations! You're ready to run the Diabetes Prediction system!**

*Start with Step 1 above and follow through to Step 4 for the complete experience.*

---

**Status:** ✅ Production Ready | **Version:** 2.0 | **Last Updated:** December 2, 2025
