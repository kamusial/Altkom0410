import matplotlib.pyplot as plt
import random

data1 = [random.randint(0,20) for i in range(1000)]  #1000 losowych liczb
data2 = [random.gauss(mu=10, sigma=5) for i in range(1000)]  # 1000 losowych liczb z rozkładu Gaussa
bins = 10  #liczba słupków

plt.subplot(2,1,1); plt.hist(data1, bins)
plt.subplot(2,1,2); plt.hist(data2, bins, facecolor="red", edgecolor='black')
plt.show()
