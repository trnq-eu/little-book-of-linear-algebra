import numpy as np
import matplotlib.pyplot as plt

v = np.array([5, 0])
w = np.array([1, -1, 4])
u = np.array([0, -3])
z = np.array([-1, 2])
q = np.array([2, 0, 0])



plt.quiver(0, 0, v[0], v[1], angles = 'xy', scale_units='xy', scale=1, color='r', label='v')
plt.quiver(0, 0, u[0], u[1], angles = 'xy', scale_units='xy', scale=1, color='b', label='u')
plt.quiver(0, 0, z[0], z[1], angles = 'xy', scale_units='xy', scale=1, color='g', label='z')
plt.quiver(0, 0, q[0], q[1], q[2], angles = 'xy', scale_units='xy', scale=1, color='y', label='q')
plt.xlim(-1, 4)
plt.ylim(-2, 4)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid()
plt.show()