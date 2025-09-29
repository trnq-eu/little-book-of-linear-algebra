import numpy as np
import matplotlib.pyplot as plt


a = 5
b = -2.5

v = np.array([4, 1])
w = np.array([1, -1, 4])

# plot vector v
plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r')
# plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='b')
plt.xlim(0, 4)
plt.ylim(-1, 4)
plt.grid()
plt.show()