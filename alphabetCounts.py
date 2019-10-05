for line in ["appAle"]:
    # print(line, end="")
    result = {}
    for char in line:
        if char.isalpha():
            char = char.lower()
            if char not in result:
                result[char] = 1
            else:
                result[char] += 1

    for key in sorted(result.keys()):
        print(key + str(result[key]), end="")