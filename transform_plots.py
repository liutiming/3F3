import numpy as np
import matplotlib.pyplot as plt
from pdfs import n_pdf
from transforms import *

transform = 1
J = 20
N = 1000
img_name = 'transform{}.png'.format(transform)

if transform == 1:
    # y = ax + b
    a = 2
    b = 4
    f = t1(a, b)
    x_rand = np.random.randn(N)
    x_lin = np.linspace(-(10 * a) / 2 + b, (10 * a) / 2 + b, N)
    plt.hist(f(x_rand), bins=J, color='cornflowerblue', density=True, label='Histogram Approximation')
    plt.plot(x_lin, n_pdf(x_lin, b, a), color='darkorange', ls='--', label='Exact Transformed Dist.') # normal plot

plt.legend()
plt.xlabel('x')
plt.ylabel('Normalised Count')
plt.savefig('C:\\Users\\obarn\\Google Drive\\Cambridge\\Part IIA\\3F3\\assets\\' + img_name)
plt.show()