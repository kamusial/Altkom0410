import matplotlib.pyplot as plt
import numpy as np

path = 'C:\\Users\\musiakam\\Desktop\\Firma\\6. Altkom\\4. Python analiza danych\\Altkom0410\\pliki\\punkty.txt'
mode = 'r'

with open(path, mode) as file:
    lines = file.readlines()

data = np.genfromtxt(lines, delimiter=',')
X = data[:,0]
Y = data[:,1]

print(data)

plt.plot(data[:,0], data[:,1], 'o')
plt.show()
