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


lista1 = [1, 2, 3, 'mama']
lista2 = ['mama', 'pies', 44.5]
lista3 = lista1 + lista2
print(lista3)
lista4 = lista1
print(lista4)

for i in range(len(lista2)):
    if lista1[i] == 'kot':
        print('znalazlem kota')

for slowo in lista1:
    if slowo == 'kot':
        print('znalazlem kota')

print('mama'.upper())
string = 'piesek'
print(string.replace('e','E', 1))

string2 = 'mama tata pies i kot'
lista_czlonkow_rodziny = string2.split()
print(lista_czlonkow_rodziny)

# x = input('Wpisz imiona i rozdziel spacja ')
# x = x.split()

def czy_dobra_kondycja(wzrost, waga, kolor_oczu = 'niebieskie'):
    if waga/wzrost**2 < 25:
        return True
    return False

def przedstaw_sie(imie, mail):
    print(f'czesc {imie}')
    print(f'wysylam maila na {mail}')

if czy_dobra_kondycja(1.7, 62):
    print('ok')


string = 'mamusia'



