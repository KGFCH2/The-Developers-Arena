Project report — LSTM time-series forecasting

Summary:
- Dataset: Synthetic series (trend + seasonality + noise), 2000 timesteps.
- Model: Single-layer LSTM (64 units) + Dense(1). Loss: MSE.
- Training: small run with early stopping; results saved to `outputs`.

What to improve next:
- Use real stock/time-series data (CSV or API).
- Hyperparameter tuning, add more layers, dropout.
- Walk-forward validation and multi-step forecasting.

Artifacts:
- `outputs/predictions.png` — visual comparison.
- `outputs/predictions.csv` — numeric results.
