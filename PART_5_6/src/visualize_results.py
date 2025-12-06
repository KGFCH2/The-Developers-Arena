# src/visualize_results.py
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

TARGET = "Outcome"

def create_prediction_visualization(X_sample, predictions, probabilities=None, save_path=None):
    if save_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(base_dir, "../models/prediction_viz.png")
    """
    Create visualization for individual predictions
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Left: Prediction results
    ax1 = axes[0]
    pred_labels = ['Non-Diabetic' if p == 0 else 'Diabetic' for p in predictions]
    colors = ['#51cf66' if p == 0 else '#ff6b6b' for p in predictions]
    bars = ax1.bar(range(len(predictions)), predictions, color=colors, alpha=0.7, edgecolor='black', linewidth=2)
    ax1.set_ylabel('Prediction (0 = Non-Diabetic, 1 = Diabetic)', fontweight='bold')
    ax1.set_xlabel('Sample Index', fontweight='bold')
    ax1.set_title('Predictions', fontweight='bold', fontsize=12)
    ax1.set_ylim(-0.1, 1.1)
    
    # Right: Probabilities
    if probabilities is not None:
        ax2 = axes[1]
        x = np.arange(len(probabilities))
        width = 0.35
        bars1 = ax2.bar(x - width/2, 1 - probabilities, width, label='Non-Diabetic', color='#51cf66', alpha=0.8, edgecolor='black')
        bars2 = ax2.bar(x + width/2, probabilities, width, label='Diabetic', color='#ff6b6b', alpha=0.8, edgecolor='black')
        ax2.set_ylabel('Probability', fontweight='bold')
        ax2.set_xlabel('Sample Index', fontweight='bold')
        ax2.set_title('Prediction Probabilities', fontweight='bold', fontsize=12)
        ax2.legend()
        ax2.set_ylim(0, 1)
        ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✅ Prediction visualization saved to: {save_path}")
    return fig

def create_feature_importance_viz(model, feature_names, save_path=None):
    if save_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(base_dir, "../models/feature_importance.png")
    """
    Create feature importance visualization
    """
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
    elif hasattr(model, 'named_steps') and 'model' in model.named_steps:
        if hasattr(model.named_steps['model'], 'feature_importances_'):
            importances = model.named_steps['model'].feature_importances_
        else:
            print("Model does not have feature importance")
            return
    else:
        print("Model does not have feature importance")
        return
    
    # Sort by importance
    indices = np.argsort(importances)[::-1]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, len(feature_names)))
    bars = ax.barh(range(len(feature_names)), importances[indices], color=colors, edgecolor='black', linewidth=1.5)
    ax.set_yticks(range(len(feature_names)))
    ax.set_yticklabels([feature_names[i] for i in indices])
    ax.set_xlabel('Importance', fontweight='bold')
    ax.set_title('Feature Importance', fontweight='bold', fontsize=14)
    
    # Add value labels
    for i, (bar, imp) in enumerate(zip(bars, importances[indices])):
        ax.text(imp + 0.005, i, f'{imp:.4f}', va='center', fontweight='bold')
    
    ax.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✅ Feature importance saved to: {save_path}")
    return fig

def create_data_distribution_viz(df, target_col=TARGET, save_path=None):
    if save_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        save_path = os.path.join(base_dir, "../models/data_distribution.png")
    """
    Create data distribution visualization
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if target_col in numeric_cols:
        numeric_cols.remove(target_col)
    
    n_cols = min(len(numeric_cols), 8)
    fig, axes = plt.subplots((n_cols + 1) // 2, 2, figsize=(14, 3*(n_cols//2 + 1)))
    axes = axes.flatten()
    
    for idx, col in enumerate(numeric_cols[:n_cols]):
        ax = axes[idx]
        diabetic = df[df[target_col] == 1][col]
        non_diabetic = df[df[target_col] == 0][col]
        
        ax.hist(non_diabetic, bins=30, alpha=0.6, label='Non-Diabetic', color='green', edgecolor='black')
        ax.hist(diabetic, bins=30, alpha=0.6, label='Diabetic', color='red', edgecolor='black')
        ax.set_xlabel(col, fontweight='bold')
        ax.set_ylabel('Frequency', fontweight='bold')
        ax.set_title(f'Distribution of {col}', fontweight='bold')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)
    
    # Hide extra subplots
    for idx in range(n_cols, len(axes)):
        axes[idx].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"✅ Data distribution saved to: {save_path}")
    return fig

if __name__ == "__main__":
    print("Generating visualizations...")
    
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "../models/final_model.joblib")
    data_path = os.path.join(base_dir, "../data/processed/test.csv")
    
    # Load model and data
    model = joblib.load(model_path)
    df = pd.read_csv(data_path)
    df = df.dropna()
    
    X = df.drop(columns=[TARGET])
    y = df[TARGET]
    
    # Get predictions
    preds = model.predict(X)
    probs = model.predict_proba(X)[:,1] if hasattr(model, "predict_proba") else None
    
    # Create visualizations
    create_prediction_visualization(X, preds, probs)
    create_feature_importance_viz(model, X.columns)
    create_data_distribution_viz(df)
    
    print("\n✅ All visualizations generated successfully!")
