# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l = self.depth(root.left)
        r = self.depth(root.right)
        return abs(l-1) > 2 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, node):
        if node is None:
            return 0
        return max(self.depth(node.left), self.depth(node.right))+1
