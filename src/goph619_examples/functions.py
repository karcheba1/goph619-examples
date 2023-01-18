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
        print(k)
        fact_k *= k     # fact_k = fact_k * k
        print(fact_k)
        t = (x ** k) / fact_k
        s += t
        print(s)
        err = abs(t / s)
    return s


if __name__ == '__main__':
    print(f'exp(0): {exp(0)}')
    print(f'exp(1): {exp(1)}')
