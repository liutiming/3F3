import numpy as np


def t1(a, b):
    """y = ax + b"""

    def f(x):
        return a * x + b

    return f


def t2():
    """y = x^2"""

    def f(x):
        return x * x

    return f


def t2_plot(x):
    y = np.zeros(len(x))
    for idx, xi in enumerate(x):
        if xi > 0.05: # Prevent very large values close to 0
            y[idx] = (1 / (np.sqrt(2 * np.pi * xi))) * np.exp(-xi / 2)
        else:
            y[idx] = 0
    return y
