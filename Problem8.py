import numpy as np
from numpy import linalg

A = np.array([[1 / 4, 1 / 4, -3 / 4, 1 / 4],
              [-3 / 4, 5 / 4, -7 / 4, 5 / 4],
              [-5 / 4, -1 / 4, 7 / 4, -1 / 4],
              [1, 0, 1, -2],
              [-1, 1, -1, 1],
              [0, -1, 0, 1]])

result = np.dot(A.transpose(), A)
print("A transpose * A is \n", result)

lambdas, V = linalg.eig(result)
print("lambda is \n", lambdas)
print("V is \n", V)

lambdas = np.delete(lambdas, 1)
print("new lambda is\n", lambdas)
V = np.delete(V, 1, 1)
print("new V is\n", V)
print(np.dot(V.transpose(), V))
S = np.sqrt(lambdas)
print("diagonal elements of S are \n", S)

prod = np.dot(A, V)
print("A * V is ", prod)

for i in range(len(S)):
    print("u", i + 1, "is\n", prod[:, i] / S[i])
