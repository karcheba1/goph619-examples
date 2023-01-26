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
    numpy.ndarray
        The result of the exponential function.
    """
    x = np.array(x)  # try to convert x to a numpy.array to check array_like
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


def cos(x):
    """Compute the value of cosine.

    Parameters
    ----------
    x : array_like
        The argument(s) to the cosine function.

    Returns
    -------
    numpy.ndarray
        The result of the cosine function.

    """
    x = np.array(x)  # try to convert x to a numpy.array to check array_like
    # initialization block
    k = 0
    fact_2k = 1
    sign = 1
    x_2 = x ** 2
    x_2k = np.ones_like(x)
    s = np.ones_like(x)
    err = np.ones_like(x)
    tol = 1.e-16
    # iteration block
    while err.max() > tol:
        k += 1
        two_k = 2 * k
        fact_2k *= two_k * (two_k - 1)  # update factorial
        sign *= -1                      # update sign, (-1) ** k
        x_2k *= x_2                  # update x ** (2 * k)
        t = sign * x_2k / fact_2k       # compute next term
        s = s + t           # increment series result
        err = abs(t / s)    # compute approximate relative error
    # return block
    return s


def sin(x):
    """Compute the value of sine.

    Parameters
    ----------
    x : array_like
        The argument(s) to the sine function.

    Returns
    -------
    numpy.ndarray
        The result of the sine function.

    """
    x = np.array(x)  # try to convert x to a numpy.array to check array_like
    # initialization block
    k = 0
    fact_2kp1 = 1
    sign = 1
    s = x
    err = np.ones_like(x)
    tol = 1.e-16
    # iteration block
    while err.max() > tol:
        k += 1
        two_k = 2 * k
        fact_2kp1 *= two_k * (two_k + 1)  # update factorial
        sign *= -1                      # update sign, (-1) ** k
        x_2kp1 = x ** (two_k + 1)
        t = sign * x_2kp1 / fact_2kp1       # compute next term
        s = s + t           # increment series result
        err = abs(t / s)    # compute approximate relative error
    # return block
    return s
