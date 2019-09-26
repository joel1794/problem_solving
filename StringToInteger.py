class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        all_digits = []
        number = ""
        digit_flag = False
        sign_flag = False
        for char in str:
            if char == " " and digit_flag:
                break
            elif char == " " and not sign_flag:
                continue

            if char == '-' and not sign_flag and not digit_flag:
                sign *= -1
                sign_flag = True
                continue
            if char == '+' and not sign_flag and not digit_flag:
                sign = 1
                sign_flag = True
                continue

            # print ord(char)
            if not (ord(char) >= ord('0') and ord(char) <= ord('9')) and not digit_flag:
                return 0
            elif not (ord(char) >= ord('0') and ord(char) <= ord('9')):
                break
            else:
                number += char
                digit_flag = True

        # print(number)
        if number == "":
            return 0
        result = int(number) * sign
        if result >= 0:
            return min(result, 2 ** 31 - 1)
        else:
            return max(result, -2 ** 31)