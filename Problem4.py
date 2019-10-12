import numpy as np
from numpy import linalg

A = np.array([[1, 2],
              [3, 1],
              [2, 3]])

prod = np.dot(A, A.transpose())
print("A * V is ", prod)

C = prod / 2
print(C)
# for i in range(len(S)):
#     print("u", i + 1, "is\n", prod[:, i] / S[i])
