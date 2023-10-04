import matplotlib.pyplot as plt

#przyklad1
numbers = [5, 10, 15, 3, 20]
# plt.plot(numbers, 'o') # niepołączone punkty
# plt.plot(numbers, '.') # niepołączone kropki
# plt.plot(numbers, 's') # niepołączone kwadraty
# plt.plot(numbers, 'ro') # czerwone punkty
# plt.plot(numbers, 'g^') # zielone trójkąty
plt.plot(numbers, 'k*') # czarne gwiazdki
# plt.plot(numbers, 'r-') # punkty połączone czerwonymi liniami
# plt.plot(numbers, 'bD:') # niebieskie diamenty połączone kropkami
# plt.plot(numbers, 'mp--') # różowe pięciokąty połączone przerywanymi liniam
plt.show()

# przyklad 2
# funkcja y = 5x - 2
X = [i+1 for i in range(10)]
Y = [5*i - 88 for i in X]
plt.plot(X, Y, 'ro-')
plt.show()

# przykład 3
# funkcja 1: y = 5x - 2 ; funkcja 2: y = -2x + 5 ; funkcja 3: y = 3x + 3
X = [i+1 for i in range(-10, 10)]
Y1 = [5*i - 2 for i in X]
Y2 = [-2*i + 5 for i in X]
Y3 = [3*i + 3 for i in X]
plt.axhline()  # linia pozioma osi
plt.axvline()  # linia pionowa osi
plt.plot(X, Y1, 'ro-')
plt.plot(X, Y2, 'b^-')
plt.plot(X, Y3, 'gs-')
#plt.plot(X,Y1,'ro-',X,Y2,'b^-',X,Y3,'gs-') # 3 ploty razem
plt.xlabel('punkty x')   #opis osi X
plt.ylabel('punkty y')   #opis osi Y
plt.title('Wykres funkcji')
plt.show()


