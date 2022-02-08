# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recurse(self, node):
        if not node:
            return 0
        left, right = self.recurse(node.left), self.recurse(node.right)
        self.result = max(self.result, left+right)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root):

        self.result = 0
        self.recurse(root)
        return self.result
