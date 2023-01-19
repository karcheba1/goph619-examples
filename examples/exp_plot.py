import numpy as np
import matplotlib.pyplot as plt

from goph619_examples.functions import (
        exp,
        )


def main():

    # generate array of x values
    x = np.linspace(-5., 5., 50)

    # compute exp(x) using our code and using numpy.exp()
    y = exp(x)
    ynp = np.exp(x)

    # plot the two sets of results
    plt.plot(x, y, 'or')
    plt.plot(x, ynp, '--k')

    # add some labels and a legend to the plot
    plt.xlabel('x')
    plt.ylabel('y = exp(x)')
    plt.legend(['goph619_examples', 'numpy'])

    # show the plot
    plt.show()


if __name__ == '__main__':
    main()
