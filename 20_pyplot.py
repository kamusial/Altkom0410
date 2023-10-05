import matplotlib.pyplot as plt

nazwy = ['nazwa1', 'nazwa2', 'nazwa3']
wartosci = [1, 10, 100]

plt.figure(figsize=(9, 3), facecolor='blue')
plt.subplot(131)
plt.bar(nazwy, wartosci)
plt.subplot(132)
plt.scatter(nazwy, wartosci)
plt.subplot(133)
plt.plot(nazwy, wartosci, linewidth=5)
plt.suptitle('cosssss')
plt.show()