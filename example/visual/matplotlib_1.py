import matplotlib.pyplot as plt

plt.rc('font', family='gulim')

plt.plot([1, 2, 3, 4, 5], [5, 9, 7, 6, 8])
plt.axis([0, 6, 4, 10])

plt.title('간단한 예제')
plt.xlabel('x축')
plt.ylabel('y축')

plt.grid()
plt.show()
