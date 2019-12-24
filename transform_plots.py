import numpy as np
import matplotlib.pyplot as plt
from pdfs import n_pdf
from transforms import *

transform = 2
J = 30
N = 1000
img_name = 'transform{}.png'.format(transform)

x_rand = np.random.randn(N)
if transform == 1:
    # y = ax + b
    a = 2
    b = 4
    f = t1(a, b)
    x_lin = np.linspace(-(10 * a) / 2 + b, (10 * a) / 2 + b, N)
    y = n_pdf(x_lin, b, a)

elif transform == 2:
    # y = x^2
    f = t2()
    x_lin = np.linspace(-4, 3, N)
    y = t2_plot(x_lin)

plt.plot(x_lin, y, color='darkorange', ls='--', label='Exact Transformed Dist.')
plt.hist(f(x_rand), bins=J, color='cornflowerblue', density=True, label='Histogram Approximation')
plt.legend()
plt.xlabel('x')
plt.ylabel('Normalised Count')
plt.savefig('C:\\Users\\obarn\\Google Drive\\Cambridge\\Part IIA\\3F3\\assets\\' + img_name)
plt.show()