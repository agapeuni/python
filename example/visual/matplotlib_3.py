import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='gulim')

x = np.arange(0, 10, 0.2)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title('사인, 코사인 그래프')
plt.xlabel('x축')
plt.ylabel('y축')
plt.legend()

plt.plot(x, y1, label="사인")
plt.plot(x, y2, label="코사인")

plt.legend()
plt.show()

