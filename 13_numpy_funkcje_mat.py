import numpy as np

a = 5
n=  0
np.radians(a), np.degrees(a)  #konwersja na radiany i stopnie
np.sin(a), np.cos(a), np.tan(a) #trygonometryczne

a = np.array([0, 45, 90, 180, 360])
b = np.radians(a)
print(b)
print(np.sin(a))
print(np.cos(a))

print('\n')
#zaokraglania
np.around(a, n) # zaokrąglanie do iluś miejsc po przecinku
np.floor(a) #w dół
np.ceil(a) #w górę

#funkcje statystyczne
# np.sum(a) - suma elementów tablicy a
# np.prod(a) - iloczyn elementów tablicy a
# np.mean(a) - średnia elementów tablicy a
# np.median(a) - mediana elementów tablicy a
# np.std(a) - odchylenie standardowe elementów tablicy a
# np.var(a) - wariancja elementów tablicy a
# np.min(a), np.max(a) - minimum i maksimum z elementów tablicy a
# np.argmin(a), np.argmax(a) - indeks wartości minimalnej i maksymalnej w tablicy a

# rozklad statystyczny
mu = 3
sigma = 0.5
N =10

X = np.random.normal(mu, sigma, N)

print(X)
print(np.mean(X), np.median(X), np.std(X), np.var(X), np.min(X), np.max(X))