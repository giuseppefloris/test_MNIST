from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv


def load_mnist_data_openml():
    mnist = fetch_openml('mnist_784', cache=True)
    x = np.array(mnist.data) / 255
    y = np.array(mnist.target, dtype=int)
    return x, y


def load_mnist_data():
    data = read_csv("https://github.com/unica-isde/isde/raw/master/data/mnist_data.csv")
    data = np.array(data)
    y = data[:, 0]
    x = data[:, 1:]
    return x, y


def plot_ten_digits(x, y=None):
    plt.figure(figsize=(20, 5))
    for i in range(10):
        plt.subplot(2, 5, i+1)
        img = x[i, :].reshape(28, 28)
        plt.imshow(img, cmap='gray')
        if y is not None:
            plt.title("label:" + str(y[i]))

    plt.show()
    return img


def split_data(x, y, n_tr, n_ts=None):
    n_samples = x.shape[0]
    idx = np.linspace(0, n_samples - 1, num=n_samples, dtype=int)
    np.random.shuffle(idx)
    if n_ts is None:
        n_ts = n_samples-n_tr
    idx_tr = idx[0: n_tr]
    idx_ts = idx[n_tr:n_ts + n_tr]
    x_tr = x[idx_tr, :]
    y_tr = y[idx_tr]
    x_ts = x[idx_ts, :]
    y_ts = y[idx_ts]
    return x_tr, y_tr, x_ts, y_ts
