# 🚀 Setup & Troubleshooting Guide

**Complete setup instructions for beginners**

---

## System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| Python | 3.10+ | 3.11+ |
| RAM | 4 GB | 8 GB |
| Disk Space | 500 MB | 1 GB |
| OS | Windows/macOS/Linux | Any |

---

## Installation Steps

### Step 1: Verify Python
```bash
python --version
# Should show 3.10 or higher
```

If not installed: https://www.python.org/downloads/

### Step 2: Navigate to Project
```bash
cd path/to/PART 5 - 6
```

### Step 3: Create Virtual Environment (Recommended)

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

**Packages installed:**
- pandas, numpy (Data processing)
- scikit-learn (Machine learning)
- matplotlib, seaborn (Visualizations)
- fastapi, uvicorn (API)
- streamlit (Web app)
- joblib (Model serialization)

---

## Running the Pipeline

### Command 1: Prepare Data
```bash
python src/data_prep.py
```
**Output:** `data/processed/train.csv` and `test.csv`

### Command 2: Train Model
```bash
python src/train.py
```
**Output:** `models/final_model.joblib`

### Command 3: Evaluate Model
```bash
python src/evaluate.py
```
**Output:** `models/evaluation_report.png`

### Command 4: Generate Visualizations
```bash
python src/visualize_results.py
```
**Output:** 3 PNG files in `models/`

### Command 5: Batch Predictions (Optional)
```bash
python src/predict.py models/final_model.joblib data/processed/test.csv
```
**Output:** `data/processed/predictions.csv`

---

## Web Applications

### Streamlit (Recommended for Beginners)
```bash
python -m streamlit run app/streamlit_app.py
```
→ Opens at `http://localhost:8501`

### REST API
```bash
python -m uvicorn app.api:app --reload
```
→ Docs at `http://localhost:8000/docs`

---

## Troubleshooting

### Python Issues

| Problem | Solution |
|---------|----------|
| `python: command not found` | Install Python from python.org |
| Wrong Python version | Use `python3` instead of `python` |
| Multiple Python versions | Use full path or virtual environment |

### Package Issues

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | `pip install -r requirements.txt` |
| `pip: command not found` | `python -m pip install -r requirements.txt` |
| Permission denied | Add `--user` flag or use virtual env |

### Model Issues

| Problem | Solution |
|---------|----------|
| Model file not found | Run `python src/train.py` first |
| Feature mismatch error | Script auto-handles this |
| Low accuracy | Check data quality |

### Port Issues

| Problem | Solution |
|---------|----------|
| Port 8501 in use | Use `--server.port 8502` |
| Port 8000 in use | Use `--port 8001` |
| Cannot connect | Check firewall settings |

### Virtual Environment Issues

| Problem | Solution |
|---------|----------|
| Cannot activate | Use correct activation command for your OS |
| Packages not found | Activate venv before installing |
| Wrong Python in venv | Delete venv and recreate |

---

## API Testing

### Using curl
```bash
curl http://localhost:8000/health
```

### Using Python
```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={
        "Pregnancies": 2,
        "Glucose": 130,
        "BloodPressure": 80,
        "SkinThickness": 25,
        "Insulin": 100,
        "BMI": 28.5,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 45
    }
)
print(response.json())
```

---

## File Outputs

After running all commands:

```
models/
├── final_model.joblib        ← Trained model
├── evaluation_report.png     ← Confusion matrix & metrics
├── feature_importance.png    ← Top features chart
├── prediction_viz.png        ← Prediction distribution
└── data_distribution.png     ← Data analysis

data/processed/
├── train.csv                 ← Training data (2048 rows)
├── test.csv                  ← Test data (512 rows)
└── predictions.csv           ← Batch prediction results
```

---

## Quick Commands

| Action | Command |
|--------|---------|
| Install packages | `pip install -r requirements.txt` |
| Prepare data | `python src/data_prep.py` |
| Train model | `python src/train.py` |
| Evaluate | `python src/evaluate.py` |
| Visualize | `python src/visualize_results.py` |
| Web app | `python -m streamlit run app/streamlit_app.py` |
| API | `python -m uvicorn app.api:app --reload` |

---

## Getting Help

1. **Check this guide** for common solutions
2. **Read error messages** - they often tell you exactly what's wrong
3. **Check file paths** - make sure you're in the right directory
4. **Restart terminal** - sometimes a fresh start helps
5. **Reinstall packages** - `pip install -r requirements.txt --force-reinstall`

---

<p align="center">
  <b>Still having issues? Check the error message carefully!</b><br>
  <i>Last Updated: December 5, 2025</i>
</p>
