from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        close_to_open = {')': '(', '}': '{', ']': '['}
        if s == "":
            return True
        if len(s) < 2:
            return False
        for c in s:
            # print(stack)
            if c in ('(', '{', '['):
                stack.append(c)
            elif c in (')', '}', ']') and stack:
                if stack.pop() != close_to_open[c]:
                    return False
            else:
                return False

        if stack:
            return False
        return True
