import matplotlib.pyplot as plt

plt.rc('font', family='gulim')

plt.plot([1, 2, 3], [6, 9, 7])
plt.axis([0, 5, 4, 10])

plt.title('간단한 예제')
plt.xlabel('x축')
plt.ylabel('y축')

plt.grid()
plt.show()