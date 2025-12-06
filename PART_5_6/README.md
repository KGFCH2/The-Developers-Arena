# 🏥 Diabetes Prediction & Analysis System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Live Demo](https://img.shields.io/badge/Live%20Demo-Diabetes%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Portfolio](https://img.shields.io/badge/Portfolio-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

> Predict diabetes risk using Advanced Machine Learning! Powered by AI for accurate, real-time health insights. 🌟

---

## 🌐 Live Demos

Experience the system in action! 🚀

- **🩺 Diabetes Prediction App**: [https://new-diabetes-prediction.streamlit.app/](https://new-diabetes-prediction.streamlit.app/)  
  Interactive web app for instant diabetes risk assessment using patient data.

- **🎨 Portfolio Website**: [https://portfolio-sigma-two-y8yfx7btmc.vercel.app/](https://portfolio-sigma-two-y8yfx7btmc.vercel.app/)  
  Showcase of projects, skills, and achievements in data science and web development.

---

## 🏆 Project Highlights

| Metric | Value |
|:---:|:---:|
| Accuracy | 85.45% 🎯 |
| Algorithm | Random Forest 🌲 |
| Status | Ready to Use ✅ |
| Deployment | Streamlit & FastAPI 🌐 |
| Live Demos | Available Online 🌍 |

---

## ⚡ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager
- Git (for cloning the repository)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/KGFCH2/The-Developers-Arena.git
   cd The-Developers-Arena/PART_5_6
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Data & Train Model**
   ```bash
   # Clean and prepare data
   python src/data_prep.py
   
   # Train the machine learning model
   python src/train.py
   
   # Evaluate model performance
   python src/evaluate.py
   ```

5. **Launch Applications**
   ```bash
   # Start Streamlit App
   streamlit run app/streamlit_app.py
   
   # Or start FastAPI backend
   uvicorn app.api:app --reload
   ```

### Docker Setup (Optional)
```bash
# Build and run with Docker
docker build -t diabetes-app .
docker run -p 8501:8501 diabetes-app
```

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

## ✨ Key Features

- **🔮 Real-time Predictions**: Input patient data and get instant diabetes risk assessment with probability scores.
- **📊 Interactive Dashboards**: Explore 3D visualizations, radar charts, and correlation heatmaps for deeper insights.
- **🎯 High Accuracy**: 85.45% accuracy using Random Forest algorithm trained on 2,048 samples.
- **🩺 Clinical Features**: Analyzes 8 key health metrics including glucose, BMI, age, and family history.
- **🌐 Web Deployment**: Fully deployed on Streamlit Cloud and Vercel for global access.
- **📱 Responsive Design**: Dark-mode friendly UI with glassmorphism effects and animations.
- **🔧 Developer-Friendly**: REST API for integration, batch predictions, and model evaluation tools.
- **📈 Advanced Analytics**: What-if simulator to see how lifestyle changes impact risk scores.
- **🎨 Portfolio Showcase**: Professional portfolio website highlighting data science projects and skills.

---

## 📸 At a Glance

### Diabetes Prediction App
- **Prediction Interface**: User-friendly form for entering patient data with sliders and instant risk visualization.
- **Analytics Dashboard**: 3D scatter plots, radar charts, and interactive heatmaps for data exploration.
- **Risk Gauge**: Dynamic gauge showing probability with color-coded risk levels.

### Portfolio Website
- **Hero Section**: Animated introduction with glitch effects and floating statistics.
- **Projects Showcase**: Glassmorphism cards with hover animations and project details.
- **Skills & Timeline**: Interactive timeline of achievements and technical skills.

*(Screenshots available in the `models/` and `portfolio/` directories)*

---

## 🛠️ Technologies Used

### Core Technologies
- **🐍 Python 3.10+**: Primary programming language for data science and web development.
- **🤖 Scikit-Learn**: Machine learning library for Random Forest model training and evaluation.
- **📊 Pandas & NumPy**: Data manipulation and numerical computing.
- **📈 Matplotlib & Seaborn**: Static data visualizations.
- **📉 Plotly**: Interactive charts and 3D visualizations.

### Web Frameworks
- **🌟 Streamlit**: Frontend web app for user interactions and real-time predictions.
- **⚡ FastAPI**: High-performance REST API for backend services.
- **🌐 HTML/CSS/JavaScript**: Portfolio website with animations and responsive design.

### Deployment & Tools
- **☁️ Streamlit Cloud**: Hosting for the diabetes prediction app.
- **🚀 Vercel**: Hosting for the portfolio website.
- **💾 Joblib**: Model serialization and loading.
- **🔧 Git & GitHub**: Version control and collaboration.

---

## 📂 Project Architecture

```
PART_5_6/
├── .gitignore              # 🛑 Git ignore rules
├── Dockerfile              # 🐳 Docker configuration
├── INSTRUCTIONS.md         # 📋 Instructions
├── LICENSE                 # 📜 License file
├── README.md               # 📖 You are here!
├── requirements.txt        # 📦 Python dependencies
├── run_portfolio.bat       # 🖥️ Portfolio runner script
├── SETUP_GUIDE.md          # 🛠️ Setup guide
│
├── src/                    # 🐍 Python Scripts
│   ├── data_prep.py        # 🧹 Data Cleaning
│   ├── train.py            # 🧠 Model Training
│   ├── evaluate.py         # 📊 Performance Report
│   ├── predict.py          # 🔮 Batch Predictions
│   ├── visualize_results.py # 📈 Charts
│   └── __pycache__/        # 🗂️ Python cache
│
├── app/                    # 🌐 Web Apps
│   ├── api.py              # ⚡ FastAPI Backend
│   ├── streamlit_app.py    # 🌟 Streamlit Frontend
│   └── __pycache__/        # 🗂️ Python cache
│
├── portfolio/              # 🎨 Showcase
│   ├── index.html          # 🏠 Main Portfolio Page
│   └── style.css           # 💅 Styling
│
├── data/                   # 💾 Data
│   ├── raw/                # 📄 Raw Data
│   │   └── diabetes.csv    # 🩸 Diabetes dataset
│   └── processed/          # ⚙️ Ready-to-train Data
│       ├── predictions.csv # 🔮 Prediction results
│       ├── test.csv        # 🧪 Test data
│       └── train.csv       # 🎓 Training data
│
├── models/                 # 🤖 Intelligence
│   └── final_model.joblib  # 📦 Saved ML Model
│
├── report/                 # 📒 Report
│   └── Final_report.md     # 📝 Final report documentation
 
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

## 🚀 Future Enhancements

- **🔬 Advanced Models**: Integration of deep learning models (CNN, LSTM) for improved accuracy.
- **📱 Mobile App**: Native mobile application for iOS and Android.
- **🌍 Multi-language Support**: Localization for global users.
- **🔒 Privacy Features**: Enhanced data privacy and GDPR compliance.
- **📊 Real-time Monitoring**: Integration with wearable devices for continuous health tracking.
- **🤝 Collaboration Tools**: Multi-user features for healthcare professionals.

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP (Python Enhancement Proposal) 8 style guidelines
- Add tests for new features
- Update documentation
- Ensure all tests pass

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

The MIT License allows free use, modification, and distribution of the code, provided that the original copyright notice is included.

---

<p align="center">
  <b>Made with ❤️ by Babin Bid</b><br>
  <i>Last Updated: December 6, 2025</i>
</p>
