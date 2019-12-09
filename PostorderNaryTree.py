"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def narypostorder(self, root, result):
        if root:
            for child in root.children:
                self.narypostorder(child, result)
            result.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.narypostorder(root, result)

        return result