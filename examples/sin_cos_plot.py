import numpy as np
import matplotlib.pyplot as plt

from goph619_examples.functions import (
        cos,
        sin,
        )


def main():

    # generate array of x values
    x = np.linspace(-5., 5., 50)

    # compute sin(x) and cos(x) using our code and using numpy.cos()
    y_cos = cos(x)
    ynp_cos = np.cos(x)
    y_sin = sin(x)
    ynp_sin = np.sin(x)

    # plot the two sets of results
    plt.subplot(2, 1, 1)
    plt.plot(x, y_cos, 'or')
    plt.plot(x, ynp_cos, '--k')

    # add some labels and a legend to the plot
    plt.ylabel('y = cos(x)')
    plt.legend(['goph619_examples', 'numpy'])

    # plot the two sets of results
    plt.subplot(2, 1, 2)
    plt.plot(x, y_sin, 'or')
    plt.plot(x, ynp_sin, '--k')

    # add some labels and a legend to the plot
    plt.ylabel('y = sin(x)')
    plt.legend(['goph619_examples', 'numpy'])

    # show the plot
    plt.show()


if __name__ == '__main__':
    main()
