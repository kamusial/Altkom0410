import time     #import biblioteki
#from time import *     #import wszystkiego z biblioteki

# print('Hello')
# time.sleep(2)
# #sleep(2)
# print('po 2 sekundach')

#generowanie danych

zmienna1 = 5
zmienna2 = 5.5
zmienna3 = '5'
moja_lista1 = []
moja_lista2 = [4, 2.2, 'Kamil', 'piesek', 343]
print(type(moja_lista2))
print(moja_lista2[2])    #wyświetlanie elementu listy
print(moja_lista2[2:4])    #slicing

moja_lista2.append(6)   #dodawanie do listy
print(moja_lista2)     #wyświetlanie listy

dane1 = []
for i in range(6, 19, 2):   #od, do, krok
    dane1.append(i+1)
print(dane1)

dane2 = []
dane2 = [   i+1    for i in range(4, 55, 3)  ]
print(dane2)

dane3 = []
dane3 = [i*i if i % 2 == 0 else 0 for i in range(5, 54, 3)]
print(dane3)