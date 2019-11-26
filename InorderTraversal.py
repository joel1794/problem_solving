# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from collections import deque
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        # if root:
        # result = self.printinorder(root, result)
        # print(root)
        while root or stack:
            # print(root)
            if root:
                stack.append(root)
                root = root.left
                continue
            root = stack.pop()
            result.append(root.val)
            root = root.right

        return result

#     def printinorder(self, root, res):
#         if root:
#             if root.left:
#                 self.printinorder(root.left, res)

#         res.append(root.val)
#         if root.right:
#             self.printinorder(root.right, res)
#         return res