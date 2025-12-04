# src/evaluate.py
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score, classification_report, confusion_matrix, roc_curve

TARGET = "Outcome"

def evaluate(model_path="models/final_model.joblib", test_path="data/processed/test.csv", save_plots=True):
    model = joblib.load(model_path)
    df = pd.read_csv(test_path)
    # Drop rows with any NaN values
    df = df.dropna()
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    preds = model.predict(X)
    probs = model.predict_proba(X)[:,1] if hasattr(model, "predict_proba") else None

    accuracy = accuracy_score(y, preds)
    cm = confusion_matrix(y, preds)
    
    print("="*50)
    print("MODEL EVALUATION RESULTS")
    print("="*50)
    print(f"Accuracy: {accuracy:.4f}")
    if probs is not None:
        roc_auc = roc_auc_score(y, probs)
        print(f"ROC AUC: {roc_auc:.4f}")
    print("\nClassification report:\n", classification_report(y, preds))
    print("Confusion matrix:\n", cm)
    print("="*50)
    
    if save_plots:
        # Create visualizations
        fig = plt.figure(figsize=(15, 10))
        
        # 1. Confusion Matrix
        ax1 = plt.subplot(2, 3, 1)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True, ax=ax1,
                    xticklabels=['Non-Diabetic', 'Diabetic'],
                    yticklabels=['Non-Diabetic', 'Diabetic'])
        ax1.set_title('Confusion Matrix', fontweight='bold', fontsize=12)
        ax1.set_ylabel('True Label')
        ax1.set_xlabel('Predicted Label')
        
        # 2. ROC Curve
        ax2 = plt.subplot(2, 3, 2)
        if probs is not None:
            fpr, tpr, _ = roc_curve(y, probs)
            roc_auc = roc_auc_score(y, probs)
            ax2.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
            ax2.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')
            ax2.set_xlim([0.0, 1.0])
            ax2.set_ylim([0.0, 1.05])
            ax2.set_xlabel('False Positive Rate')
            ax2.set_ylabel('True Positive Rate')
            ax2.set_title('ROC Curve', fontweight='bold', fontsize=12)
            ax2.legend(loc="lower right")
            ax2.grid(alpha=0.3)
        
        # 3. Accuracy Metrics
        ax3 = plt.subplot(2, 3, 3)
        tn, fp, fn, tp = cm.ravel()
        sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
        specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        f1 = 2 * (precision * sensitivity) / (precision + sensitivity) if (precision + sensitivity) > 0 else 0
        
        metrics = ['Accuracy', 'Sensitivity', 'Specificity', 'Precision', 'F1-Score']
        values = [accuracy, sensitivity, specificity, precision, f1]
        colors = plt.cm.viridis(np.linspace(0, 1, len(metrics)))
        bars = ax3.barh(metrics, values, color=colors, edgecolor='black', linewidth=1.5)
        ax3.set_xlim(0, 1)
        ax3.set_xlabel('Score')
        ax3.set_title('Performance Metrics', fontweight='bold', fontsize=12)
        for i, (bar, val) in enumerate(zip(bars, values)):
            ax3.text(val + 0.02, i, f'{val:.3f}', va='center', fontweight='bold')
        ax3.grid(axis='x', alpha=0.3)
        
        # 4. Prediction Distribution
        ax4 = plt.subplot(2, 3, 4)
        if probs is not None:
            ax4.hist(probs[y == 0], bins=20, alpha=0.6, label='Non-Diabetic', color='green', edgecolor='black')
            ax4.hist(probs[y == 1], bins=20, alpha=0.6, label='Diabetic', color='red', edgecolor='black')
            ax4.set_xlabel('Prediction Probability')
            ax4.set_ylabel('Frequency')
            ax4.set_title('Prediction Probability Distribution', fontweight='bold', fontsize=12)
            ax4.legend()
            ax4.grid(axis='y', alpha=0.3)
        
        # 5. Classification Results Pie Chart
        ax5 = plt.subplot(2, 3, 5)
        correct = (preds == y).sum()
        incorrect = (preds != y).sum()
        colors_pie = ['#51cf66', '#ff6b6b']
        ax5.pie([correct, incorrect], labels=['Correct', 'Incorrect'],
                autopct='%1.1f%%', colors=colors_pie, startangle=90,
                textprops={'fontweight': 'bold'})
        ax5.set_title('Overall Classification Accuracy', fontweight='bold', fontsize=12)
        
        # 6. Confusion Matrix Percentages
        ax6 = plt.subplot(2, 3, 6)
        cm_percent = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis] * 100
        sns.heatmap(cm_percent, annot=True, fmt='.1f', cmap='YlOrRd', cbar=True, ax=ax6,
                    xticklabels=['Non-Diabetic', 'Diabetic'],
                    yticklabels=['Non-Diabetic', 'Diabetic'])
        ax6.set_title('Confusion Matrix (% per class)', fontweight='bold', fontsize=12)
        ax6.set_ylabel('True Label')
        ax6.set_xlabel('Predicted Label')
        
        plt.tight_layout()
        plt.savefig('models/evaluation_report.png', dpi=300, bbox_inches='tight')
        print("\n✅ Evaluation report saved to: models/evaluation_report.png")
        plt.show()

if __name__ == "__main__":
    evaluate()
