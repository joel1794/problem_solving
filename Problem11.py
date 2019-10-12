import numpy as np
from numpy import linalg

X = np.array([[2, -1, 0, 1, 1, -3, 5, 2], [-2, 3, 2, 3, 0, 2, -1, 1], [-1, 3, 3, 1, -1, 4, 5, 2], [3, -1, 0, 3, 2, -1, 3, 0]])

XT = X.transpose()
mean = [0] * len(XT)
# print(XT)
for i in range(len(XT)):
    mean[i] = sum(XT[i, :])/len(XT[i, :])

XT = XT.astype(float)
mean = np.array(mean)
# print(XT)
print(mean)
for i in range(len(XT)):
    XT[i, :] = np.subtract(XT[i, :], mean[i])

print(XT)
print(XT.shape)
covariance_matrix = np.dot(XT, XT.transpose())
# print(covariance_matrix)
covariance_matrix /= len(XT[0])
print(covariance_matrix)
lambdas, U = linalg.eigh(covariance_matrix)
print("lambdas are\n", lambdas.round(3))
print("U is\n", U.round(3))

lambdas = lambdas[5:8]
U = U[:, 5:8]
U = np.dot(U, -1)
print("lambdas are\n", lambdas.round(3))
print("U is\n", U.round(3))


delta = []

for j in range(len(U[0])):
    delta.append([0] * len(XT[0]))

delta = np.array(delta)
delta = delta.astype(float)
# print("delta is\n", delta)

for i in range(len(U[0])):
    for j in range(len(XT[0])):
        delta[i][j] = np.dot(XT[:, j], U[:, i])


print("delta is\n", delta.round(2))

Y = np.array([[1, 5, 1, 5, 5, 1, 1, 3], [-2, 3, 2, 3, 0, 2, -1, 1], [2, -3, 2, 3, 0, 0, 2, -1], [2, -2, 2, 2, -1, 1, 2, 2]])
YT = Y.transpose()
YT = YT.astype(float)
# print(YT)
for i in range(len(YT)):
    YT[i, :] = np.subtract(YT[i, :], mean[i])

print("Y after subtracting mean\n", YT)

W = []
for j in range(len(U[0])):
    W.append([0] * len(YT[0]))
W = np.array(W)
W = W.astype(float)
print("W initialized\n", W)

for i in range(len(U[0])):
    for j in range(len(YT[0])):
        # print(U[i, :], YT[j, :])
        W[i][j] = np.dot(U[:, i], YT[:, j])
        # print(W)

print("W result\n", W)

min_delta_test = []
for i in range(len(delta[0])):
    min_dist = 99999
    for j in range(len(delta[0])):
        # print(training_delta[:, j], delta[:, i])
        euc_dist = np.linalg.norm(delta[:, j] - W[:, i])
        # print(euc_dist)
        if euc_dist < min_dist:
            min_dist = euc_dist
    print('{0:.2f}'.format(min_dist))