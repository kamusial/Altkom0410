import numpy as np

A = np.array([[1,2],[3,4]])
print(A)

detA1 = A[0,0]*A[1,1] - A[1,0]*A[0,1]
detA2 = np.linalg.det(A)

print(detA1, detA2)

trA1 = A[0,0] + A[1,1]
trA2 = np.trace(A)
print(trA1, trA2)

print('\n')
# wartości własne i wektory własne macierzy
m = np.array([[1, 2, 3],
              [2, 3, 4],
              [4, 5, 9]])
eigenvalues, eigenvectors = np.linalg.eig(m)
print(eigenvalues, eigenvectors)
print('\n')
# macierz odwrotna i transpozycja
mI = np.linalg.inv(m)
mT = np.transpose(m)
print(mI, mT)

#cwiczenie
A = np.array([[2, 3], [4, 1]])
B = np.array([12, 14])

XY = np.linalg.solve(A, B)
print(XY)

XY = np.linalg.inv(A) @ B
print(XY)

#Dla układów sprzecznych / nieoznaczonych funkcja nie zadziała i program nie wykona się poprawnie.