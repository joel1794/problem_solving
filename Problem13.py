import numpy as np
from numpy import linalg

malware = np.array([[1, -1, 1, -1, -1, 1], [-2, 2, 2, -1, -2, 2], [1, 3, 0, 1, 3, 1], [2, 3, 1, 1, -2, 0]])
benign = np.array([[-1, 2, 1, 2, -1, 0], [-2, 1, 2, 3, 2, 1], [-1, 3, 0, 1, 3, -1], [0, 2, 3, 1, 1, -2]])
test = np.array([[1, 5, 1, 5, 5, 1], [-2, 3, 2, 3, 0, 2], [2, -3, 2, 3, 0, 0], [2, -2, 2, 2, -1, 1]])

unit_eigenvectors = np.array([[0.16408622, 0.62780739, -0.26039808, -0.53891957, 0.46372117, 0.0751984],
                     [0.2443382, 0.1070203, -0.80167357, 0.42774159, -0.1373179, -0.29042369]])
training_delta = np.array([[-1.1069, 1.2793, -2.6800, 2.5076], [1.5480, 0.5484, -1.2085, -0.8879]])

malware = malware.transpose()
benign = benign.transpose()
test = test.transpose()
unit_eigenvectors = unit_eigenvectors.transpose()

# print(malware, "\n", benign, "\n", test)

# mean = [0] * len(malware)
# print(XT)
# for i in range(len(malware)):
#     mean[i] = sum(malware[i, :])/len(malware[i, :])

mean = np.array([7/4, 7/4, 5/4, 2, 2, 1])
malware = malware.astype(float)
benign = benign.astype(float)
test = test.astype(float)
# mean = np.array(mean)
print("mean to be subtracted is\n", mean)
for i in range(len(malware)):
    malware[i, :] = np.subtract(malware[i, :], mean[i])

for i in range(len(benign)):
    benign[i, :] = np.subtract(benign[i, :], mean[i])

for i in range(len(test)):
    test[i, :] = np.subtract(test[i, :], mean[i])

print("malware data after subtracting mean is\n", malware)
print("benign data after subtracting mean is\n", benign)
print("test data after subtracting mean is\n", test)
# covariance_matrix = np.dot(malware, malware.transpose())
# # print(covariance_matrix)
# covariance_matrix /= len(malware[0])
# print("covariance matrix of malware is\n", covariance_matrix)
# lambdas, U = linalg.eig(covariance_matrix)
#
# print("lambdas are\n", lambdas.round(3))
# print("U is\n", U.round(3))
#
# lambdas = lambdas[0:3]
# U = U[:, 0:3]
# U = np.dot(U, -1)

# print("lambdas are\n", lambdas.round(3))
# print("U is\n", U.round(3))

W_malware = []
W_benign = []
W_test = []

for j in range(len(training_delta)):
    W_malware.append([0] * len(training_delta[0]))
    W_benign.append([0] * len(training_delta[0]))
    W_test.append([0] * len(training_delta[0]))

W_malware = np.array(W_malware)
W_malware = W_malware.astype(float)
W_benign = np.array(W_benign)
W_benign = W_benign.astype(float)
W_test = np.array(W_test)
W_test = W_test.astype(float)
# print("delta is\n", delta)

# print("malware after subtracting mean is\n", malware)
# print("benign samples after subtracting mean is\n", benign)
# print("test samples after subtracting mean is\n", test)
# print("unit eigen vectors are\n", unit_eigenvectors)

for i in range(len(unit_eigenvectors[0])):
    for j in range(len(malware[0])):
        # print(malware[:, j], unit_eigenvectors[:, i])
        W_malware[i][j] = np.dot(malware[:, j], unit_eigenvectors[:, i])
        # print(W_malware)

for i in range(len(unit_eigenvectors[0])):
    for j in range(len(benign[0])):
        # print(benign[:, j], unit_eigenvectors[:, i])
        W_benign[i][j] = np.dot(benign[:, j], unit_eigenvectors[:, i])
        # print(W_benign)

for i in range(len(unit_eigenvectors[0])):
    for j in range(len(test[0])):
        # print(benign[:, j], unit_eigenvectors[:, i])
        W_test[i][j] = np.dot(test[:, j], unit_eigenvectors[:, i])
        # print(W_benign)

# print("training delta is\n", training_delta.round(2))
print("W malware is\n", W_malware.round(2))
print("W benign is\n", W_benign.round(2))
print("W test is\n", W_test.round(2))

min_delta_test = []
for i in range(len(W_test[0])):
    min_dist_malware = 99999
    min_dist_benign = 99999

    for j in range(len(W_malware[0])):
        # print(training_delta[:, j], W_malware[:, i])
        euc_dist = np.linalg.norm(W_malware[:, j] - W_test[:, i])
        # print(euc_dist.round(2))
        if euc_dist < min_dist_malware:
            min_dist_malware = euc_dist
            # print(training_delta[:, j], W_malware[:, i].round(2))
            # print(euc_dist.round(2))

    for j in range(len(W_benign[0])):
        # print(training_delta[:, j], W_malware[:, i])
        euc_dist = np.linalg.norm(W_benign[:, j] - W_test[:, i])
        # print(euc_dist.round(2))
        if euc_dist < min_dist_benign:
            min_dist_benign = euc_dist
            # print(training_delta[:, j], W_malware[:, i].round(2))
            # print(euc_dist.round(2))
    if min_dist_malware < min_dist_benign:
        print("nearest euclidean distance with malware sample is ", min_dist_malware.round(2))
        print("Y", i + 1, " is malware")
    else:
        print("nearest euclidean distance with benign sample is ", min_dist_benign.round(2))
        print("Y", i + 1, " is benign")
    # print('{0:.2f}'.format(min_dist))