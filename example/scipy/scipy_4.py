import numpy as np
from scipy.stats import ttest_ind

a = (56, 128.6, 12, 123.8, 64.34, 78, 763.3)
b = (1.1, 2.9, 4.2)
print(ttest_ind(a, b, trim=.2))
print()

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)
print(v1)
print(v2)
print()

res1 = ttest_ind(v1, v2).statistic
res2 = ttest_ind(v1, v2).pvalue
print('statistic =', res1)
print('pvalue =:', res2)

