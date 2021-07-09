import matplotlib.pyplot as plt
import numpy as np

r = np.arange(0, 20, 1)

plt.plot(  r, r*2,         # line
           r, r*2.5, '--'  # dotted line
         , r, r*3, '^'     # triangle
         , r, r*3.5, 'v'   # triangle
         , r, r*4, '<'     # triangle
         , r, r*4.5, '>'   # triangle
         , r, r*5, 's'     # square
         , r, r*5.5, 'd'   # square(dice)
         , r, r*6, 'p'     # pentagon
         , r, r*6.5, 'h'   # hexagon
         , r, r*7, 'o'     # circle
         , r, r*7.5, '+'   # cross
         , r, r*8, '*'     # star
         , r, r*8.5, 'x'   # cross
         , r, r*9, '.'     # big dot
         , r, r*9.5, ','   # small dot
         )
plt.show()      