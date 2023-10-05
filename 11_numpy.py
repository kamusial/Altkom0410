import numpy as np

list1 = [4, 5, 6, 7]
array1 = np.array(list1)
print(array1)
print(type(array1))

print(array1[2])
print(array1[:2])
array1[2] = 50
print(array1)
print('dlugosc ',len(array1))

for i in array1:
    print(i)

np.zeros(5)    #lista o długości 5 wypełniona zerami
np.ones(5)      #lista o długości 5 wypełniona jedynkami
np.empty(5)    #lista o długości 5 wypełniona "zerowymi" wartościami"

x = np.linspace(0, 10, 5)    #od, do, ile elementów
print(x)

x = np.arange(0, 0.5, 0.1)    #od, do krok
print(x)

x = np.random.randint(-10, 10, 5)   #od, do, ile
print(x)

#tablice N-wymiarowe
x = np.array(10)    #0-wymiarowa
a = np.array([1, 2, 3, 4, 5, 6])   #1-wymiarowa
m = np.array( [  [2, 3, 4],  [5, 6, 7]   ])    #2-wymiarowa
print(m)
print('\n')
t = np.array([ [ [2, 3, 4],[5,6,7]   ] , [ [12, 13, 41], [15, 16, 17]   ]  ])
print(t)
print(t[1])
print(t[1][1])
print(t[1][1][2])
print('\noperacje na elementach tablicy')
#operacje na elementach tablicy

a = np.array([1, 2, 5, 11, 20])
b = np.array([4, 5, 6, 10, 40])

c = a + b
print(c)
d = a - b
print(d)
e = a * b
print(e)

f = a + 100
print(f)
g = a * 10
print(g)

np.ones([2, 2])
np.zeros([5, 3])
m = np.identity(4)
print(m)


