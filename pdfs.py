import numpy as np


def n_pdf(x, mu=0., sigma=1.):  # normal pdf - does this function need to be inside ksd?
    """Returns a value y corresponding to the value of the normal distribution at input x"""
    u = (x - mu) / abs(sigma)
    y = (1 / (np.sqrt(2 * np.pi) * abs(sigma)))
    y *= np.exp(-u * u / 2)
    return y


def u_pdf(a, b):
    return 1/(b - a)