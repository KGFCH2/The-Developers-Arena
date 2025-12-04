# CNN Image Classification on CIFAR-10

This project implements a Convolutional Neural Network (CNN) for image classification using the CIFAR-10 dataset. The model is trained to classify images into 10 different categories: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, and truck.

## Features

- Simple CNN architecture with 3 convolutional layers
- Trained on CIFAR-10 dataset (60,000 32x32 color images)
- Achieves ~72% test accuracy
- Includes model evaluation with classification report and confusion matrix
- Saves training history plots

## Requirements

- Python 3.7+
- TensorFlow 2.x
- NumPy
- Matplotlib
- Scikit-learn

## Installation

1. Ensure Python is installed on your system.
2. Install the required packages:

```bash
pip install tensorflow numpy matplotlib scikit-learn
```

## Usage

### Training the Model

Run the training script:

```bash
python train_cnn.py --epochs 20 --batch_size 128
```

- `--epochs`: Number of training epochs (default: 20)
- `--batch_size`: Batch size for training (default: 128)

### What the Script Does

1. Loads and preprocesses the CIFAR-10 dataset
2. Builds a CNN model architecture
3. Trains the model on the training data
4. Evaluates the model on test data
5. Saves the trained model as `cnn_cifar10_model.h5`
6. Generates evaluation results in `evaluation_results.txt`
7. Creates training history plot as `training_history.png`

## Files

- `train_cnn.py`: Main training script
- `cnn_cifar10_model.h5`: Trained CNN model (generated after training)
- `evaluation_results.txt`: Model performance metrics (generated after training)
- `training_history.png`: Training curves plot (generated after training)

## Results

After training, the model achieves approximately 72% accuracy on the test set. The evaluation results include:

- Overall accuracy
- Precision, recall, and F1-score for each class
- Confusion matrix
- Training history plots

## Notes

- Training may take several minutes depending on your hardware
- The model uses a basic CNN architecture suitable for beginners
- For better performance, consider using data augmentation or more complex architectures like ResNet

## License

This project is for educational purposes.