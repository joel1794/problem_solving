import numpy as np

A = np.array([[1 / 4, 1 / 4, -3 / 4, 1 / 4],
              [-3 / 4, 5 / 4, -7 / 4, 5 / 4],
              [-5 / 4, -1 / 4, 7 / 4, -1 / 4],
              [1, 0, 1, -2],
              [-1, 1, -1, 1],
              [0, -1, 0, 1]])
n = 4
result = np.dot(A, A.transpose())
# print("A transpose * A is \n", result)
result *= 1/n
print("1/n * A transpose * A is \n", result)

variance_input = 0
for i in range(len(result)):
    for j in range(len(result[0])):
        if i == j:
            variance_input += result[i][j]

print("variance in input is\n", variance_input)

variance_projection = 0
U = [[0.16408622, -0.2443382, 0.07100155], [0.62780739, -0.1070203, -0.29337893], [-0.26039808, 0.80167357, -0.39519489], [-0.53891957, -0.42774159, -0.34390332], [0.46372117, 0.1373179, -0.36438048], [0.0751984, 0.29042369, 0.70828381]]

# U_column_sums = [0] * len(U[0])
# for i in range(len(U)):
#     for j in range(len(U[0])):
#         U_column_sums[j] += U[i][j]
# print("column sums of U is \n", U_column_sums)

eigenvalues = [4.0833, 1.2364, 0.7428]
for value in eigenvalues:
    variance_projection += value

print("varaince in projected space is\n", variance_projection)

print(4.0833/variance_projection)
print((4.0833 + 1.2364)/variance_projection)
print((4.0833 + 1.2364 + 0.7428)/variance_projection)

# sum(l)/ sum(k) where l is most dominant eigenvalues and k is non trivial eigenvalues

