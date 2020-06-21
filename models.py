import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def split_dataset(dataset, seed=1):
    """
    Split dataset into train (70%), validation (15%), test (15%).
    """
    X = dataset.drop(columns=['pid', 'window10', 'timestamp', 'intoxicated'], axis=1)
    y = dataset[['intoxicated']]
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=seed)
    valid_X, test_X, valid_y, test_y = train_test_split(test_X, test_y, test_size=0.5, random_state=seed)
    return train_X, valid_X, test_X, train_y, valid_y, test_y


def plot_confusion_matrix(test_y, y_pred):
    """
    Given test_y and y_predictions, plot confusion matrix.
    """
    cm = confusion_matrix(test_y, y_pred)
    fig, ax = plt.subplots()
    ax.matshow(cm)
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')

    for (i, j), z in np.ndenumerate(cm):
        ax.text(j, i, '{:d}'.format(z), ha='center', va='center')

    plt.show()


