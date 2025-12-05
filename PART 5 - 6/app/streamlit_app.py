# app/streamlit_app.py
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Diabetes Predictor", layout="wide")
st.title("🏥 Diabetes Prediction Demo")
st.markdown("---")

# Load model
model = joblib.load("models/final_model.joblib")

# Create two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📋 Enter Patient Features")
    preg = st.number_input("Pregnancies", value=0.0, step=1.0)
    glucose = st.number_input("Glucose", value=120.0)
    bp = st.number_input("BloodPressure", value=70.0)
    skin = st.number_input("SkinThickness", value=20.0)
    insulin = st.number_input("Insulin", value=79.0)
    bmi = st.number_input("BMI", value=25.0)
    dpf = st.number_input("DiabetesPedigreeFunction", value=0.467)
    age = st.number_input("Age", value=33.0)

with col2:
    st.markdown("### 📊 Results Visualization")
    predict_clicked = st.button("🔮 Predict", key="predict_btn")

if predict_clicked:
    df = pd.DataFrame([{
        "Pregnancies": preg, "Glucose": glucose, "BloodPressure": bp,
        "SkinThickness": skin, "Insulin": insulin, "BMI": bmi,
        "DiabetesPedigreeFunction": dpf, "Age": age, "BMI_age_ratio": bmi / (age + 1e-6)
    }])
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0,1] if hasattr(model, "predict_proba") else None
    
    # Display prediction results with color coding
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Prediction Result")
        pred_text = "🔴 **DIABETIC** (High Risk)" if int(pred) == 1 else "🟢 **NON-DIABETIC** (Low Risk)"
        st.markdown(pred_text, unsafe_allow_html=True)
    
    with col2:
        if prob is not None:
            st.markdown("#### Probability")
            st.markdown(f"**{prob:.1%}** risk of diabetes")
    
    # Create visualization of prediction
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        # Bar chart for probability
        fig, ax = plt.subplots(figsize=(6, 4))
        if prob is not None:
            categories = ['Diabetic', 'Non-Diabetic']
            values = [prob*100, (1-prob)*100]
            colors = ['#ff6b6b', '#51cf66']
            bars = ax.barh(categories, values, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
            
            # Add value labels
            for i, (bar, val) in enumerate(zip(bars, values)):
                ax.text(val + 2, i, f'{val:.1f}%', va='center', fontweight='bold', fontsize=11)
            
            ax.set_xlim(0, 100)
            ax.set_xlabel('Probability (%)', fontweight='bold')
            ax.set_title('Prediction Confidence', fontweight='bold', fontsize=12)
            ax.grid(axis='x', alpha=0.3)
        st.pyplot(fig, use_container_width=True)
    
    with col2:
        # Gauge visualization
        fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(projection='polar'))
        theta = np.linspace(0, np.pi, 100)
        r = np.ones(100)
        ax.plot(theta, r, 'gray', lw=2)
        
        # Color zones
        theta_green = np.linspace(0, 0.3*np.pi, 50)
        theta_red = np.linspace(0.7*np.pi, np.pi, 50)
        ax.fill_between(theta_green, 0, 1, alpha=0.3, color='green')
        ax.fill_between(theta_red, 0, 1, alpha=0.3, color='red')
        
        # Pointer
        if prob is not None:
            pointer_angle = np.pi * (1 - prob)
            ax.plot([pointer_angle, pointer_angle], [0, 1], 'k-', lw=3)
        
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['polar'].set_visible(False)
        ax.set_title("Risk Probability Gauge", pad=20, fontsize=12, fontweight='bold')
        st.pyplot(fig, use_container_width=True)
    
    # Display patient profile
    st.markdown("---")
    st.markdown("#### 👤 Patient Profile")
    patient_data = {
        'Feature': ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'],
        'Value': [preg, glucose, bp, skin, insulin, bmi, dpf, age]
    }
    patient_df = pd.DataFrame(patient_data)
    st.dataframe(patient_df, use_container_width=True)
