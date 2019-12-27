import numpy as np
import matplotlib.pyplot as plt
from smoothing import ksdensity


def f(x):
    return np.exp(-x)


def inverse(y):
    return -np.log(1 - y)


smoothed = False # Toggle histogram and smoothed plot

J = 20
N = 1000
x_rand = np.random.rand(N)
x_lin = np.linspace(0, 5, N)
if smoothed:
    ksdensity = ksdensity(inverse(x_rand), width=0.3)
    plt.plot(x_lin, ksdensity(x_lin), color='cornflowerblue',
             label='Smoothed Approximation')
else:
    plt.hist(inverse(x_rand), bins=J, color='cornflowerblue',
             density=True, label='Histogram Approximation')
plt.plot(x_lin, f(x_lin), color='darkorange', ls='--',
         label='Exact Dist.')
plt.legend()
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.show()
