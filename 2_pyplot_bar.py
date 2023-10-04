import matplotlib.pyplot as plt
import random

names = [
    'Joanna',
    'Dagmara',
    'Ania',
    'Zosia',
    'Zusia'
]
ages = [random.randint(2, 70) for name in names]

plt.bar(names, ages, color=['red', 'green', 'blue'])
plt.xticks(names)
plt.yticks(ages)
plt.show()