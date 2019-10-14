class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """Brute Force approach
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[j] < nums[i]:
                    continue

                for k in range(j + 1, len(nums)):
                    # print(nums[i], nums[j], nums[k])
                    if nums[j] > nums[k] > nums[i]:
                        return True
        return False
        """
        """improved brute force
        min_num = 999
        for i in range(len(nums) - 1):
            # keet track of minimum element
            if nums[i] < min_num:
                min_num = nums[i]                
            for j in range(i + 1, len(nums)):
                # print(j, j + 1)
                # print(min_num, nums[i], nums[j]) 
                if nums[i] > nums[j] > min_num:
                    return True
        return False
        """
        """stack implementation"""
        min_nums = []
        if nums:
            min_val = max(nums)
        for num in nums:
            if num < min_val:
                min_val = num
            min_nums.append(min_val)
        print(min_nums)

        stack = []
        # print(not stack)
        for i in range(len(nums) - 1, -1, -1):
            # print("j", j)
            if (nums[i] > min_nums[i]):
                while stack and stack[len(stack) - 1] <= min_nums[i]:
                    stack.pop()
                # print(nums[i], stack, min_nums[i])
                if stack and nums[i] > stack[len(stack) - 1] > min_nums[i]:
                    return True
                stack.append(nums[i])

        return False

