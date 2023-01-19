def exp(x):
    """
    """
    k = 0
    fact_k = 1
    err = 1.
    tol = 1e-16
    s = 1.
    while err > tol:
        k += 1
        fact_k *= k     # fact_k = fact_k * k
        t = (x ** k) / fact_k
        s += t
        err = abs(t / s)
    return s
