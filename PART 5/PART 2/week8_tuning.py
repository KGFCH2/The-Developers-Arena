# week8_tuning.py
# Model Evaluation and Hyperparameter Tuning example using RandomForest on Iris
# Usage: python week8_tuning.py

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def run_tuning():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(random_state=42)
    param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [2, 4, 6, None]}
    grid = GridSearchCV(clf, param_grid, cv=5, n_jobs=-1)
    grid.fit(X_train, y_train)
    print('Best parameters:', grid.best_params_)
    y_pred = grid.predict(X_test)
    print('\nClassification report:\n', classification_report(y_test, y_pred))
    print('\nConfusion matrix:\n', confusion_matrix(y_test, y_pred))

if __name__ == '__main__':
    run_tuning()
