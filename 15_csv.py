import matplotlib.pyplot as plt

path = 'C:\\Users\\musiakam\\Desktop\\Firma\\6. Altkom\\4. Python analiza danych\\Altkom0410\\pliki\\punkty.txt'
mode = 'r'

with open(path, mode) as file:
    lines = file.readlines()

data = []
for line in lines:
    x, y = line.split(',')
    data.append([int(x), int(y)])

print(data)
X = [record[0] for record in data]
Y = [record[1] for record in data]

plt.plot(X, Y, 'o')
plt.show()

