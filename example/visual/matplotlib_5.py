import matplotlib.pyplot as plt
import numpy

t = numpy.arange(0., 5., 1.)

plt.grid()

lines = plt.plot(t, t*2,color = '#cccfff', linewidth=3)
plt.setp(lines, color='#cccfff', linewidth=2.0)
plt.setp(lines, 'color', 'r', 'linewidth', 3.0)

plt.show()