import numpy as np
import matplotlib.pyplot as plt
import math


def n_pdf(x, mu=0., sigma=1.):  # normal pdf - does this function need to be inside ksd?
    """Returns a value y corresponding to the value of the normal distribution at input x"""
    u = (x - mu) / abs(sigma)
    y = (1 / (np.sqrt(2 * np.pi) * abs(sigma)))
    y *= np.exp(-u * u / 2)
    return y


def u_pdf(a, b):
    return 1/(b - a)


def integ(f, a, b, dx=0.01):
    """Retuns a trapezium rule approximation of an integral"""
    tot = 0
    for i in np.arange(a, b, dx):
        tot += f(i) * dx
    return tot


# print(integ(n_pdf,0.,1)*1000/n_pdf(0.5))

dist = 'u'

if dist == 'n':
    # Plot normal distribution
    bins = 30
    x_range = 10
    N = 1000
    x_rand = np.random.randn(N)
    x_lin = np.linspace(-(x_range / 2), x_range / 2, N)

    plt.hist(x_rand, bins=bins, color='blue', density=True)
    plt.xlabel('x')
    plt.ylabel('count')
    plt.plot(x_lin, n_pdf(x_lin), color='red')  # Only approximate scaling
    plt.show()

elif dist == 'u':
    # Plot uniform distribution
    bins = 20
    x_rand = np.random.rand(1000)
    plt.hist(x_rand, bins=bins, color='blue', density=True)
    plt.plot([0, 1], [u_pdf(0, 1), u_pdf(0, 1)], color='red')  # Scaled to match data exactly
    plt.xlabel('x')
    plt.ylabel('count')
    plt.show()
