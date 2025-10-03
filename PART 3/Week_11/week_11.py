# Week 11 – Neural Network for MNIST Digit Classification
# --------------------------------------------------------

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

# -----------------------------
# 1. Load MNIST dataset
# -----------------------------
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print("Training data shape:", x_train.shape)
print("Test data shape:", x_test.shape)

# -----------------------------
# 2. Preprocess data
# -----------------------------
# Normalize pixel values (0–255 → 0–1)
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# Flatten images (28x28 → 784)
x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

# -----------------------------
# 3. Build Neural Network
# -----------------------------
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),   # hidden layer 1
    layers.Dense(64, activation='relu'),                        # hidden layer 2
    layers.Dense(10, activation='softmax')                      # output layer for 10 digits
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print(model.summary())

# -----------------------------
# 4. Train the model
# -----------------------------
history = model.fit(
    x_train, y_train,
    validation_split=0.1,
    epochs=10,
    batch_size=32,
    verbose=2
)

# -----------------------------
# 5. Evaluate model
# -----------------------------
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\n✅ Test Accuracy: {test_acc*100:.2f}%")

# -----------------------------
# 6. Confusion Matrix
# -----------------------------
y_pred = np.argmax(model.predict(x_test), axis=-1)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix – MNIST NN")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

print("\nClassification Report:\n", classification_report(y_test, y_pred))

# -----------------------------
# 7. Plot Training History
# -----------------------------
plt.figure(figsize=(6,4))
plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Training vs Validation Accuracy')
plt.show()

# -----------------------------
# 8. Save the model
# -----------------------------
model.save("mnist_nn_model.h5")
print("Model saved as mnist_nn_model.h5")
