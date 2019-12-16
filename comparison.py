import numpy as np
import matplotlib.pyplot as plt
from pdfs import n_pdf, u_pdf
from smoothing import ksdensity


dist = 'u'
smoothed = True
width = 0.4


def uniform_plot(a, b):
    p = u_pdf(a, b)
    range = b - a
    plt.plot([a, b], [p, p], color='darkorange', ls='--')
    plt.plot([a - range / 4, a], [0, 0], color='darkorange', ls='--')
    plt.plot([b, b + range / 4], [0, 0], color='darkorange', ls='--')
    plt.plot([a, a], [0, p], color='darkorange', ls='--')
    plt.plot([b, b], [0, p], color='darkorange', ls='--')


def normal_plot(x_axis):
    plt.plot(x_axis, n_pdf(x_axis), color='darkorange', ls='--')


if dist == 'n':
    # Plot normal distribution
    bins = 30
    x_range = 10
    N = 1000
    x_rand = np.random.randn(N)
    x_lin = np.linspace(-(x_range / 2), x_range / 2, N)
    if smoothed:
        ks_density = ksdensity(x_rand, width=width)
        plt.plot(x_lin, ks_density(x_lin)/width, color='cornflowerblue')
        img_name = 'smoothed_normal.png'
    else:
        plt.hist(x_rand, bins=bins, color='cornflowerblue', density=True)
        img_name = 'normal_comparison.png'
    normal_plot(x_lin)

elif dist == 'u':
    # Plot uniform distribution
    a = 0
    b = 1
    p = u_pdf(a, b)
    bins = 20
    N = 1000
    x_rand = np.random.rand(N)
    x_lin = np.linspace(-0.5, 1.5, N)
    if smoothed:
        ks_density = ksdensity(x_rand, width=width)
        plt.plot(x_lin, ks_density(x_lin)/width, color='cornflowerblue')
        img_name = 'smoothed_uniform.png'
    else:
        plt.hist(x_rand, bins=bins, color='cornflowerblue', density=True)
        img_name = 'uniform_comparison.png'
    uniform_plot(a, b)
    # normal_plot(x_lin)

plt.xlabel('x')
plt.ylabel('Normalised Count')
plt.savefig('C:\\Users\\obarn\\Google Drive\\Cambridge\\Part IIA\\3F3\\assets\\' + img_name)
plt.show()
