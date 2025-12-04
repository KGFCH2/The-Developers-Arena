import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import tensorflow as tf
# Use tf.keras attributes via the existing tensorflow import to avoid IDE import resolution issues
Sequential = tf.keras.models.Sequential
LSTM = tf.keras.layers.LSTM
Dense = tf.keras.layers.Dense
EarlyStopping = tf.keras.callbacks.EarlyStopping

RNG = np.random.RandomState(42)

def generate_series(n_steps=2000):
    t = np.arange(n_steps)
    trend = 0.0005 * t
    seasonal = 0.5 * np.sin(0.02 * t) + 0.2 * np.sin(0.005 * t * 2)
    noise = 0.2 * RNG.randn(n_steps)
    series = 10 + trend + seasonal + noise
    return pd.Series(series, name="value")


def create_sequences(values, window_size):
    X, y = [], []
    for i in range(len(values) - window_size):
        X.append(values[i : i + window_size])
        y.append(values[i + window_size])
    return np.array(X), np.array(y)


def build_model(window_size):
    model = Sequential([
        LSTM(64, input_shape=(window_size, 1)),
        Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse")
    return model


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "outputs")
    os.makedirs(out_dir, exist_ok=True)

    series = generate_series(n_steps=2000)
    df = pd.DataFrame({"value": series})

    window = 50
    split_ratio = 0.8

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df[["value"]]).flatten()

    X, y = create_sequences(scaled, window)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    split_idx = int(len(X) * split_ratio)
    X_train, y_train = X[:split_idx], y[:split_idx]
    X_test, y_test = X[split_idx:], y[split_idx:]

    tf.random.set_seed(42)
    model = build_model(window)
    early = EarlyStopping(monitor="val_loss", patience=5, restore_best_weights=True)

    history = model.fit(
        X_train,
        y_train,
        validation_data=(X_test, y_test),
        epochs=30,
        batch_size=32,
        callbacks=[early],
        verbose=1,
    )

    preds_scaled = model.predict(X_test).flatten()
    preds = scaler.inverse_transform(preds_scaled.reshape(-1, 1)).flatten()
    y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1)).flatten()

    mse = mean_squared_error(y_test_inv, preds)
    print(f"Test MSE: {mse:.6f}")

    results_df = pd.DataFrame({"true": y_test_inv, "pred": preds})
    results_csv = os.path.join(out_dir, "predictions.csv")
    results_df.to_csv(results_csv, index=False)

    # Plot a segment
    plt.figure(figsize=(10, 5))
    idx_show = slice(0, 300)
    plt.plot(results_df.index[idx_show], results_df["true"].iloc[idx_show], label="True")
    plt.plot(results_df.index[idx_show], results_df["pred"].iloc[idx_show], label="Predicted")
    plt.legend()
    plt.title(f"LSTM predictions (MSE={mse:.6f})")
    plot_path = os.path.join(out_dir, "predictions.png")
    plt.tight_layout()
    plt.savefig(plot_path)
    print(f"Saved plot to: {plot_path}")
    print(f"Saved CSV to: {results_csv}")


if __name__ == "__main__":
    main()
