# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.ans = 0

        def helper(node):
            if node:
                helper(node.right)
                self.ans += node.val
                node.val = self.ans
                helper(node.left)
        helper(root)
        return root
