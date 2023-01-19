import numpy as np
import matplotlib.pyplot as plt

from goph619_examples.functions import (
        exp,
        )


def main():

    x = np.linspace(-5., 5., 10)
    y = np.zeros(x.shape)
    for k, xk in enumerate(x):
        y[k] = exp(xk)

    plt.plot(x, y)

    plt.show()


if __name__ == '__main__':
    main()
