for line in ["2", "5", "12"]:
    # print(line, end="")
    line = int(line)
    if line == 0:
        print(0)
    elif line == 1:
        print(1)
    else:
        num1 = 0
        num2 = 1
        num = 0
        for i in range(line - 1):
            num = num1 + num2
            num1 = num2
            num2 = num
        print(num)
