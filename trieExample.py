def minimumLengthEncoding(words):
    root = dict()
    leaves = []
    for word in set(words):
        cur = root
        for i in word[::-1]:
            print(i)
            print(cur.get(i, dict()))
            cur[i] = cur.get(i, dict())
            cur = cur[i]
            # cur[i] = cur
        print("leaves before append", leaves)
        leaves.append((cur, len(word) + 1))
        print("leaves after append", leaves)
        print(root)
    print("root at end", root)
    print("leaves at end", leaves)
    return sum(depth for node, depth in leaves if len(node) == 0)


print(minimumLengthEncoding(["me", "time"]))
print(minimumLengthEncoding(["time", "time", "time", "time"]))