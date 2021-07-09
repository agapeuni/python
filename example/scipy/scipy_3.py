import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
    [2, 2],
    [2, 7],
    [3, 4],
    [3.5, 6],
    [4, 1],
    [4, 5],
    [5, 3],
    [5, 6]
])


simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()
