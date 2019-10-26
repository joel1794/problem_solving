def splitTheArray(val):
    num_of_splits = 0
    for i in range(len(val)):
        for j in range(i + 1, len(val) - 1):
            sub_arrays = []
            sub_arrays.append(val[0: j + 1])
            sub_arrays.append(val[j + 1: len(val)])
            # print(sub_arrays)
    return num_of_splits

splitTheArray([1,2,3,4])