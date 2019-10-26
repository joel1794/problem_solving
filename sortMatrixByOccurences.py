def sortMatrixByOccurences(m):
    occurence_dict = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] not in occurence_dict:
                occurence_dict[m[i][j]] = 0
            occurence_dict[m[i][j]] += 1
    # sorted(occurence_dict)
    # print(occurence_dict)
    sorted_occurence = sorted(occurence_dict.items(), key=lambda x: (-x[1], x[0]))
    new_sorted_occurence = []
    for element in sorted_occurence:
        for count in range(element[1]):
            new_sorted_occurence.append(element[0])
    print(new_sorted_occurence)
    # print(sorted_occurence)
    new_matrix = []
    for i in range(len(m)):
        new_matrix.append([0] * len(m[0]))
    # print(new_matrix)

    i = 0
    j = 0
    list_index = 0
    # print("list index is ", list_index)
    down = True
    diagonal = False
    ROW = len(new_matrix)
    COL = len(new_matrix[0])
    for line in range(1, (ROW + COL)):
        start_col = max(0, line - ROW)
        count = min(line, (COL - start_col), ROW)

        for j in range(0, count):
            new_matrix[min(ROW, line) - j - 1][start_col + j] = new_sorted_occurence[list_index]
            list_index += 1


    return new_matrix

print(sortMatrixByOccurences([[1, 4, -2], [-2, 3, 4], [3, 1, 3]]))




# diagonalOrder([[1, 4, -2], [-2, 3, 4], [3, 1, 3]])