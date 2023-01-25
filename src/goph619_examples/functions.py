"""A module for implementing functions with series solutions in Python.

Contains functions: exp()
"""

import numpy as np


def exp(x):
    """The exponential function.

    Parameters
    ----------
    x : array_like
        The argument(s) to the exponential function.

    Returns
    -------
    float or numpy.ndarray
        The result of the exponential function.
    """
    x = np.array(x)  # try to convert x to a numpy.ndarry to check array_like
    # initialization block
    k = 0
    fact_k = 1
    x_k = np.ones_like(x)
    s = np.ones_like(x)
    err = np.ones_like(x)
    tol = 1.e-16
    # iteration block
    while err.max() > tol:
        k += 1          # increment iteration counter, k = k + 1
        fact_k *= k     # update factorial, fact_k = fact_k * k
        x_k *= x        # update x ** k, by multiplying by x
        t = x_k / fact_k    # compute term in series
        s = s + t           # increment series result
        err = abs(t / s)    # compute approximate relative error
    # return block
    return s
