import numpy as np
import matplotlib.pyplot as plt


def n_pdf(x, mu=0., sigma=1.):  # normal pdf - does this function need to be inside ksd?
    """Returns a value y corresponding to the value of the normal distribution at input x"""
    u = (x - mu) / abs(sigma)
    y = (1 / (np.sqrt(2 * np.pi) * abs(sigma)))
    y *= np.exp(-u * u / 2)
    return y


def ksdensity(data, width=0.3):
    """Returns kernel smoothing function from data points in data"""

    def ksd(x_axis):
        prob = [n_pdf(x_i, data, width) for x_i in x_axis]
        pdf = [np.average(pr) for pr in prob]  # each row is one x value
        return np.array(pdf)

    return ksd


dist = 'u'

if dist == 'n':
    # Plot normal distribution
    bins = 30
    max_count = 1000
    x_rand = np.random.randn(max_count)
    x_lin = np.linspace(-5, 5, max_count)
    ks_density = ksdensity(x_rand, width=0.4)


elif dist == 'u':
    # Plot uniform distribution
    bins = 20
    max_count = 1000
    x_rand = np.random.rand(max_count)
    x_lin = np.linspace(-1.5, 1.5, max_count)
    ks_density = ksdensity(x_rand, width=0.2)

fig, ax1 = plt.subplots()
color = 'tab:blue'
ax1.plot(x_lin, ks_density(x_lin))
ax1.set_xlabel('x')
ax1.set_ylabel('count')
ax2 = ax1.twinx()
color = 'tab:orange'
ax2.plot(x_lin, n_pdf(x_lin), color=color)  # Only approximate scaling
ax2.set_ylabel('p')
plt.show()
