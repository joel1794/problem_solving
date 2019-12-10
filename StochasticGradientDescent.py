import numpy as np
import math

X = [[0.6, 0.4], [0.1, 0.2], [0.8, 0.6], [0.3, 0.7], [0.7, 0.3], [0.7, 0.7], [0.2, 0.9]]
# X = [[1, 0], [0, 0], [1, 1], [0, 1], [1, 0], [1, 1], [0, 1]]
# X = np.array(X)
Z = [1, 0, 0, 1, 1, 0, 1]
# Z = np.array(Z)
w = [1, 2, -1, 1, -2, 1]

v = [0 for i in range(13)]
# v = np.array(v)
learning_rate = 0.1
dv = [0 for i in range(12)]

def forwardpass(X, input_class):
    # print("Z is", Z)
    # print("v is", v)
    v[0:6] = w
    # print(v)

    v[6] = X[0] * v[0] + X[1] * v[2]
    v[7] = X[0] * v[1] + X[1] * v[3]

    v[8] = 1 + math.exp(-v[6])
    v[9] = 1 + math.exp(-v[7])

    v[10] = v[4] / v[8]
    v[11] = v[5] / v[9]
    # print(len(v))

    v[12] = math.pow((v[10] + v[11] - input_class), 2) / 2
    z = v[12]

def backwardpass(X, input_class):
    dz = 1
    dv[11] = dv[10] = v[10] + v[11] - input_class
    dv[10] = dv[10] = v[10] + v[11] - input_class
    dv[9] = -(v[5] / (v[9] * v[9])) * dv[11]
    dv[8] = -(v[4] / (v[8] * v[8])) * dv[10]
    dv[7] = -(math.exp(-v[7])) * dv[9]
    dv[6] = -(math.exp(-v[6])) * dv[8]
    dv[5] = dv[11] / v[9]
    dv[4] = dv[10] / v[8]
    dv[3] = X[1] * dv[7]
    dv[2] = X[1] * dv[6]
    dv[1] = X[0] * dv[7]
    dv[0] = X[0] * dv[6]

def score(X):
    v[0:6] = w
    # print(v)

    v[6] = X[0] * v[0] + X[1] * v[2]
    v[7] = X[0] * v[1] + X[1] * v[3]

    v[8] = 1 + math.exp(-v[6])
    v[9] = 1 + math.exp(-v[7])

    v[10] = v[4] / v[8]
    v[11] = v[5] / v[9]
    # print(len(v))

    # v[12] = math.pow((v[10] + v[11] - input_class), 2) / 2
    z = v[10] + v[11]

    return z

def accuracy(predictions, ground_truth):
    missed = 0
    for i in range(len(predictions)):
        if predictions[i] != ground_truth[i]:
            missed += 1

    return 100 - missed * 100 / len(predictions)

def compute_output(X, weights):
    return (weights[4] / (1 + math.exp(-(w[0] * X[0] + w[2] * X[1])))) + (weights[5] / (1 + math.exp(-(w[1] * X[0] + w[3] * X[1]))))

for i in range(1000):
    for j in range(len(X)):
        # print("dv is", dv)
        # print("epoch", i, X[j])
        forwardpass(X[j], Z[j])
        backwardpass(X[j], Z[j])

        for k in range(len(w)):
            w[k] -= learning_rate * dv[k]

print("weights after training are", w)
train_pred = [0 for i in range(len(Z))]

for i in range(len(X)):
    # print(score(X[i]))
    if score(X[i]) >= 0.5:
        train_pred[i] = 1
    else:
        train_pred[i] = 0

# train_pred_1 = [0 for i in range(len(Z))]
#
# for i in range(len(X)):
#     # print(score(X[i]))
#     # print(compute_output(X[i], w))
#     if compute_output(X[i], w) > 0.5:
#         train_pred_1[i] = 1
#     else:
#         train_pred_1[i] = 0

print(train_pred)
# print(train_pred_1)
print(Z)
print(accuracy(train_pred, Z))

X1 = [[0.55, 0.11], [0.32, 0.21], [0.24, 0.64], [0.86, 0.68], [0.53, 0.79], [0.46, 0.54], [0.16, 0.51], [0.52, 0.94], [0.46, 0.87], [0.96, 0.63]]
Z1 = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

test_pred = [0 for i in range(len(Z1))]
for i in range(len(X1)):
    # print(score(X[i]))
    if score(X1[i]) >= 0.5:
        test_pred[i] = 1
    else:
        test_pred[i] = 0

print(test_pred)
print(Z1)
print(accuracy(test_pred, Z1))

w = [1, 2, -1, 1, -2, 1]
for i in range(10000):
    for j in range(len(X)):
        # print("dv is", dv)
        # print("epoch", i, X[j])
        forwardpass(X[j], Z[j])
        backwardpass(X[j], Z[j])

        for k in range(len(w)):
            w[k] -= learning_rate * dv[k]

print("weights after training are", w)
train_pred = [0 for i in range(len(Z))]

for i in range(len(X)):
    # print(score(X[i]))
    if compute_output(X[i], w) >= 0.5:
        train_pred[i] = 1
    else:
        train_pred[i] = 0

print(train_pred)
# print(train_pred_1)
print(Z)
print(accuracy(train_pred, Z))

X1 = [[0.55, 0.11], [0.32, 0.21], [0.24, 0.64], [0.86, 0.68], [0.53, 0.79], [0.46, 0.54], [0.16, 0.51], [0.52, 0.94], [0.46, 0.87], [0.96, 0.63]]
Z1 = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

test_pred = [0 for i in range(len(Z1))]
for i in range(len(X1)):
    # print(score(X[i]))
    if compute_output(X1[i], w) >= 0.5:
        test_pred[i] = 1
    else:
        test_pred[i] = 0

print(test_pred)
print(Z1)
print(accuracy(test_pred, Z1))
