import matplotlib.pyplot as plt

expenses = ["mieszkanie", "media", "jedzenie", "rozrywka", "nauka", "inwestycje"]
values = [3000, 300, 1000, 500, 200, 1500]

explode = [0 for i in expenses]
explode[expenses.index('inwestycje')] = 0.2

plt.pie(values, labels=expenses,
        explode=explode,   # wyróznienie elementu
        autopct="%.2f %%",   # wartości procentowe
        shadow=True)    #cień do wykresu
plt.show()

