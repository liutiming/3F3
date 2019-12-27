import math

import matplotlib.pyplot as plt
import numpy as np

from smoothing import ksdensity


def f(x, alpha=1):
    return (alpha ** 2) / 2 * np.exp(-(alpha ** 2 * x) / 2)


def inverse(y):
    return -np.log(1 - y)


alpha = 0.5
N = 1000
J = 30

normal_x = np.random.randn(N)
px_u = np.zeros(len(normal_x))  # Conditional
pxu = np.zeros(len(normal_x))  # Joint
x_lin = np.linspace(-1, 1, N)

for idx, xi in enumerate(normal_x):
    u = inverse(np.random.rand())
    px_u[idx] = math.sqrt(u) * xi
    pxu[idx] = px_u[idx] * f(u, alpha=alpha)

plt.hist(pxu, bins=J, color='cornflowerblue',
         density=True, label='Histogram Approximation')
ks_density = ksdensity(pxu, width=0.1)
smoothed = ks_density(x_lin)
log_smoothed = np.log(smoothed)
plt.plot(x_lin, smoothed, color='darkorange',
         label='Smoothed Approximation')
plt.plot(x_lin, log_smoothed, color='darkorange',
         label='Smoothed Approximation')
plt.legend()
plt.xlabel('x')
plt.ylabel('Normalised Count')
plt.show()
