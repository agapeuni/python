import matplotlib.pyplot as plt
import numpy as np

r = np.arange(0, 10, 1)

plt.plot(  r, r * 2, 'r--'  # red line
         , r, r * 3, 'g--'  # green
         , r, r * 4, 'b--'  # blue
         , r, r * 5, 'y--'  # yellow
         , r, r * 6, 'c--'  # cyan
         , r, r * 7, 'm--'  # magenta
         , r, r * 8, 'w--'  # white
         , r, r * 9, 'k--'  # black
         )
plt.show()

