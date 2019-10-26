def findMaxLength(nums) -> int:
    # longest_subarray = []
    # print(nums)
    max_length = 0
    for i in range(len(nums)):
        # longest_subarray = []
        # longest_subarray.append(nums[i])
        # print("i values is ", i)
        # print((len(nums) - i) % 2)
        max_length = 0
        no_contiguous_flag = False
        if (len(nums) - i) % 2 != 0:
            continue
        # print((i + len(nums)) / 2)
        for j in range(i, int((i + len(nums)) / 2)):
            # print("j values is ", j)
            # print("start is ", j, "and end is ", len(nums) - 1 - (j - i))
            if nums[j] != nums[len(nums) - 1 - (j - i)]:
                # longest_subarray.append(nums[j])
                # print("longest  contiguous subarray for given i ", i, " is ", longest_subarray)
                max_length += 2
            else:
                no_contiguous_flag = True
                break
        # print("value of j after loop is ", j)
        # print("max length is ", max_length)
        # print(no_contiguous_flag)
        if not no_contiguous_flag:
            return max_length

    return max_length

print(findMaxLength([0, 1, 0]))
