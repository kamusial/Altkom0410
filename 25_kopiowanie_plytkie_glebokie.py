slownik = {'jeden': 1, 'dwa': 2, 'trzy': 3}
lista1 = [slownik, 4, 5, 6]


def zmiany(lista):
    lista[1] = 40
    lista[0]['jeden'] = 10

def zmiany2(lista):
    lista.append(4)
    lista.append(5)
    lista.append(6)

from copy import deepcopy
print(lista1)
zmiany(deepcopy(lista1))
print(lista1)

lista2 = [1, 2, 3]
print(lista2)
zmiany2(lista2[:])
print(lista2)

lista3 = lista2
lista3.append('cos')
print(lista2)

