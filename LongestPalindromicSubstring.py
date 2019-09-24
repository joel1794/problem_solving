class Solution(object):
    def palindromCheck(self, s, i, j):
        while (i > -1 and j < len(s) and s[i] == s[j]):
            i -= 1
            j += 1
        return j - i - 1
        # # print "strin received is " + s
        # n = len(s)
        # if n % 2 == 0:
        #     j = n / 2
        #     i =  j - 1
        # else:
        #     j = (n / 2) + 1
        #     i = (n / 2) - 1
        # # print "".join(reversed(s[j : n + 1]))
        # if s[0 : i + 1] != "".join(reversed(s[j : n + 1])):
        #     return False
        # # while (j < n):
        # #     if s[i] == s[j]:
        # #         i -= 1
        # #         j += 1
        # #     else:
        # #         return False
        # return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length_of_palindrome = 0
        palindrom_string = ""
        n = len(s)
        # max_len = 0
        i_max = 0
        j_max = 0
        for i in range(n):
            # for j in range(i + 1, n + 1):
            len1 = self.palindromCheck(s, i, i)
            len2 = self.palindromCheck(s, i, i + 1)
            len_max_for_1_pass = max(len1, len2)
            if len_max_for_1_pass > j_max - i_max:
                j_max = i + (len_max_for_1_pass / 2)
                i_max = i - (len_max_for_1_pass - 1) / 2

        return s[i_max: j_max + 1]
        # if not sol:
        #     continue
        # else:
        #     if j - i > length_of_palindrome:
        #     length_of_palindrome = j - i
        #     palindrom_string = s[i:j]

        # return palindrom_string