import numpy as np
import matplotlib.pyplot as plt
from pdfs import u_pdf
import math

N = [100, 1000, 10000]
J = 20
a = 0
b = 1
p = u_pdf(a, b)

fig, ax = plt.subplots(3, figsize=(10, 15))

for i in range(3):
    mu = N[i]/J
    sigma = mu * math.sqrt((J - 1)/N[i])
    x_rand = np.random.rand(N[i])
    ax[i].hist(x_rand, bins=J, color='cornflowerblue')
    ax[i].set_ylabel('Count')
    ax[i].axhline(mu, color='red', ls='--')
    ax[i].axhline(0, color='black')
    ax[i].axhline(mu - sigma, color='darkorange', ls='--')
    ax[i].axhline(mu + sigma, color='darkorange', ls='--')
    ax[i].axhline(mu - sigma, color='darkorange', ls='--')
    ax[i].axhline(mu + 3 * sigma, color='gold', ls='--')
    ax[i].axhline(mu - 3 * sigma, color='gold', ls='--')

plt.xlabel('x')
plt.savefig('C:\\Users\\obarn\\Google Drive\\Cambridge\\Part IIA\\3F3\\assets\\uniforms.png')
plt.show()
