import matplotlib.pyplot as plt
import numpy as np


mu = -4
sigma = 1

def gaussian():
	u1 = np.random.rand(1)
	u2 = np.random.rand(1)

	z1 = (np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2))
	return z1 * sigma + mu

z = []
for i in range(100):
	z.append(gaussian()[0])
print(z)
plt.hist(z, 50)
plt.show()
