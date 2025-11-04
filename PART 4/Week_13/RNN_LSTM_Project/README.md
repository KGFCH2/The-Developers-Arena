RNN / LSTM — Time-Series Forecasting Example

This small project demonstrates training a compact LSTM model on a synthetic "stock-like" time series (trend + seasonality + noise). It is intended as a hands-on example you can use as a starting point for real-world forecasting tasks.

What you'll find here
- `train_lstm.py` — End-to-end script that generates the synthetic series, prepares sequences, trains a Keras LSTM, and saves prediction artifacts.
- `requirements.txt` — Minimal dependencies to run the script.
- `report.md` — Short project summary and suggested next steps.

Quick start (Windows cmd.exe)

1. Create or activate your Python environment and install dependencies:

```bat
python -m pip install -r requirements.txt
```

2. Run the training script:

```bat
python train_lstm.py
```

Outputs
- The script writes artifacts to the `outputs/` folder inside the project directory:
	- `predictions.csv` — CSV with two columns: `true` and `pred` (test set true values and model predictions).
	- `predictions.png` — Plot comparing true vs predicted values for a segment of the test set.

How to use this as a starting point
- To train on real data, replace the synthetic `generate_series()` call in `train_lstm.py` with a loader that reads your CSV (timestamp + value). Keep the sequence creation (`create_sequences`) and scaler logic, or adapt for multivariate inputs.
- Consider the following improvements:
	- Walk-forward (rolling) validation or time-series cross validation.
	- Hyperparameter tuning (window size, LSTM units, learning rate, batch size).
	- Add dropout/regularization and experiment with stacked LSTMs or GRUs.

Notes
- The example trains quickly and uses early stopping; reported Test MSE is printed by the script after training.
- If your Python executable path contains spaces, run the script explicitly with the full quoted path, e.g.:

```bat
"C:\\Program Files\\Python313\\python.exe" train_lstm.py
```

License
- MIT-style (feel free to adapt for your use).

If you'd like, I can:
- Add a version that reads a CSV of historical stock prices.
- Convert this into a Jupyter notebook with inline plots and interactive analysis.
- Add unit tests for the sequence creation and scaler inverse operations.

Happy to make one of these next — tell me which you'd prefer.
