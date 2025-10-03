# Week 9 – Random Forest Classifier with User Input
# --------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

# -----------------------------
# 1. Load dataset
# -----------------------------
data = pd.read_csv("customer_churn.csv")
data = data.drop(columns=['CustomerID'])  # drop ID

# -----------------------------
# 2. Encode categorical variables
# -----------------------------
cat_cols = data.select_dtypes(include='object').columns
data_encoded = pd.get_dummies(data, columns=cat_cols, drop_first=True)

# Split into features & target
X = data_encoded.drop('Churn', axis=1)
y = data_encoded['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# 3. Train Random Forest
# -----------------------------
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

print("Model trained successfully ✅")

# -----------------------------
# 4. User Input Section
# -----------------------------
print("\n--- Enter Customer Details for Prediction ---")
tenure = int(input("Tenure Months: "))
monthly_charges = float(input("Monthly Charges: "))
total_charges = float(input("Total Charges: "))
contract = input("Contract (Month-to-month / One year / Two year): ")
payment = input("Payment Method (Credit card / Bank transfer / Electronic check / Mailed check): ")
internet = input("Internet Service (DSL / Fiber optic / No): ")
tech = input("Tech Support (Yes / No): ")
tv = input("Streaming TV (Yes / No): ")

# Build a dataframe for user input
user_df = pd.DataFrame([{
    'TenureMonths': tenure,
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges,
    'Contract': contract,
    'PaymentMethod': payment,
    'InternetService': internet,
    'TechSupport': tech,
    'StreamingTV': tv
}])

# One-hot encode user input with same columns as training
user_encoded = pd.get_dummies(user_df, columns=cat_cols, drop_first=True)

# Align columns (add missing cols as 0)
user_encoded = user_encoded.reindex(columns=X.columns, fill_value=0)

# -----------------------------
# 5. Prediction
# -----------------------------
prediction = rf_model.predict(user_encoded)[0]
prob = rf_model.predict_proba(user_encoded)[0][1]

if prediction == 1:
    print(f"\n⚠️ This customer is likely to CHURN (probability: {prob:.2f})")
else:
    print(f"\n✅ This customer is NOT likely to churn (probability: {prob:.2f})")
