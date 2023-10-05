import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 100, 15

x = mu + sigma * np.random.randn(10000)

plt.hist(x, 50, facecolor='g', alpha=0.8, density=True)
plt.xlabel('Cos')
plt.ylabel('probability')
plt.title('Histogram')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid()
plt.show()