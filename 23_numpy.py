import numpy as np
array1 = np.arange(10) * 2
print(array1)

array2 = np.arange(9).reshape(3, 3)
print(array2)

array3 = np.arange(18).reshape(3, 3, 2)
print(array3)

print(array2[2])  #ostatni wiersz
print(array2[2][2])  #ostatni element
print(array2[:,2])  #ostatnia kolumna
print(array2[:2, :2])  #lewy górny róg, 2x2