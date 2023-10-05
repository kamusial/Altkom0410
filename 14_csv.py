import matplotlib.pyplot as plt

path1 = 'C:\\Users\\musiakam\\Desktop\\Firma\\6. Altkom\\4. Python analiza danych\\Altkom0410\\pliki\\rozliczenie.csv'
path2 = r'C:\Users\musiakam\Desktop\Firma\6. Altkom\4. Python analiza danych\Altkom0410\pliki\rozliczenie.csv'
mode = 'r'

with open(path2, mode) as plik1:
    # #content1 = plik1.read()   #odczyt całego pliku, jako string
    # content2 = plik1.read(5)   #odczyt 5 pierwszych bądź kolejnych znaków
    # content3 = plik1.read(5)
    # content4 = plik1.read(5)
    # content5 = plik1.readline()  #czyta linie, pierwszą bądź kolejną
    # content6 = plik1.readline()
    content7 = plik1.readlines() #czyta wszystkie linie

#print(content1)
# print(content2)
# print(content3)
# print(content4)
# print(content5)
# print(content6)
print(content7)

for i in range(len(content7)):
#    print(content7[i])
    content7[i] = content7[i].split(',')
#    print(content7[i])

print(content7)
print(content7[4])
print(content7[3][4])
print(content7[0][1][:3])

#srednia wyplata
lista_wyplat = []
total = 0
for i in range(1,len(content7)):
    total += int(content7[i][1])
    lista_wyplat.append(int(content7[i][1]))
print(f'srednia wyplata wynosi {total / (len(content7)-1)} PLN')


plt.hist(lista_wyplat, 20)
plt.show()
