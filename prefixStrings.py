def prefixString(a, b):
    l = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            if i == j:
                l.append(a[i])
            else:
                l.append(a[i] + a[j])


    # print(l)

    for sequence in b:
        if sequence not in l:
            return False
    return True

# print(prefixString(["onetwo", "two", "three"], ["onetwo", "one"]))
