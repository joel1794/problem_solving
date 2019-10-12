import numpy as np

unit_eigenvectors = [[0.16408622, 0.62780739, -0.26039808, -0.53891957, 0.46372117, 0.0751984],
                     [0.2443382, 0.1070203, -0.80167357, 0.42774159, -0.1373179, -0.29042369]]

# print(unit_eigenvectors)

Y = [[2, 3, 1, 0, 3, 2], [-4, -5, 0, 3, 1, -2], [2, 3, 0, 1, 3, 2], [3, 2, 1, 0, 3, 2]]

training_delta = np.array([[-1.1069, 1.2793, -2.6800, 2.5076], [1.5480, 0.5484, -1.2085, -0.8879]])

Y = np.array(Y)
Y = Y.astype(float)
mean = np.array([7/4, 7/4, 5/4, 2, 2, 1])

print("mean is ", mean)
for i in range(len(Y)):
    Y[i, :] = np.subtract(Y[i, :], mean)

print("Y after subtracting mean is\n", Y)
# for i in range(len(unit_eigenvectors)):
#     print(np.dot(unit_eigenvectors[i], X))
#
# for i in range(len(unit_eigenvectors)):
#     print(np.dot(unit_eigenvectors[i], X1))


delta = []
for j in range(len(unit_eigenvectors)):
    delta.append([0] * len(Y))

for i in range(len(unit_eigenvectors)):
    for j in range(len(Y)):
        # print(unit_eigenvectors[i], Y[j])
        delta[i][j] = np.dot(unit_eigenvectors[i], Y[j])
        # print(delta)

delta = np.array(delta)
print("delta is\n", training_delta)
print("W of test data is\n", delta)

min_delta_test = []
for i in range(len(delta[0])):
    min_dist = 99999
    for j in range(len(delta[0])):
        # print(training_delta[:, j], delta[:, i])
        euc_dist = np.linalg.norm(training_delta[:, j] - delta[:, i])
        # print(euc_dist)
        if euc_dist < min_dist:
            min_dist = euc_dist
    print('{0:.10f}'.format(min_dist))
