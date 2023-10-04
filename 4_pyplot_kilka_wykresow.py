import matplotlib.pyplot as plt
import random
import math

X = [x for x in range(0, 360+1, 10)]
Y1 = [math.cos(math.radians(i)) for i in X]
Y2 = [random.random() for i in X]
Y3 = [random.random() for i in X]
Y4 = [random.random() for i in X]
plt.subplot(2,2,1) # poziomy,piony,index
plt.plot(X,Y1,"r.-")

plt.subplot(2,3,3) # poziomy,piony,index
plt.plot(X,Y2,"bs:")

plt.subplot(2,2,3) # poziomy,piony,index
plt.plot(X,Y3,"r.-")

plt.subplot(2,2,4) # poziomy,piony,index
plt.plot(X,Y4,"bs:")
plt.show()