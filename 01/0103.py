import numpy as np
import matplotlib.pyplot as plt

v = np.array([2, 3])
u = np.array([1, -1])

sum_vector = v + u
print("v + u =", sum_vector)


plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='r', label='v')
plt.quiver(v[0], v[1], u[0], u[1], angles='xy', scale_units='xy', scale=1, color='b', label='u placed at end of v')
plt.quiver(0, 0, sum_vector[0], sum_vector[1], angles='xy', scale_units='xy', scale=1, color='g', label='v + u')

plt.xlim(-1, 5)
plt.ylim(-2, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.show()