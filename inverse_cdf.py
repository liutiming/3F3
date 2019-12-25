import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(-x)

def inverse(y):
    return -np.log(1-y)

J = 20
N = 1000
x_rand = np.random.rand(N)
x_lin = np.linspace(0, 5, N)
plt.hist(inverse(x_rand), bins=J, color='cornflowerblue', density=True, label='Histogram Approximation')
plt.plot(x_lin, f(x_lin), color='darkorange', ls='--', label='Exact Dist.')  # normal plot
plt.legend()
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.savefig('C:\\Users\\obarn\\Google Drive\\Cambridge\\Part IIA\\3F3\\assets\\inverse_cdf.png')
plt.show()