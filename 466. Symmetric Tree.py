"""
I started by checking that can we invert a binary tree and see it's 
val are same or not but it will be not eff so Let's use recursion to solve 
this and check for left.left and right.right, left.right and right.left vals 
to be equal
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val != right.val:
            return False
        a = self.check(left.left, right.right)
        b = self.check(left.right, right.left)
        return a and b
