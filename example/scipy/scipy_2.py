import numpy as np
from scipy.sparse import csr_matrix

print(csr_matrix((3, 4), dtype=np.int8).toarray())
print()
print(csr_matrix(np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])))
