from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

n = 150
xmin, xmax, ymin, ymax, zmin, zmax = 0, 30, 0, 40, 0, 50
cmin, cmax = 0, 3

color = np.array([(cmax - cmin) * np.random.random_sample() + cmin for i in range(n)])
xs = np.array([(xmax - xmin) * np.random.random_sample() + xmin for i in range(n)])
ys = np.array([(ymax - ymin) * np.random.random_sample() + ymin for i in range(n)])
zs = np.array([(zmax - zmin) * np.random.random_sample() + zmin for i in range(n)])

plt.rcParams["figure.figsize"] = (6, 6)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, c=color, marker='o', s=20, cmap='Greens')

plt.show()
