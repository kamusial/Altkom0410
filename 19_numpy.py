import matplotlib.pyplot as plt
import numpy as np

data = {'a': np.arange(50),
        'c': np.random.randint(100, 104, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * data['d']
data['d'] = np.abs(data['d']) * 100

#plt.scatter(data['a'], data['b'])
plt.scatter('a', 'b', data=data, c='c', s='d')
plt.xlabel('os x')
plt.ylabel('os y')
plt.show()