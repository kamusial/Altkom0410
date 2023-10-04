import matplotlib.pyplot as plt

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
