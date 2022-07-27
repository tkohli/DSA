"""
Nice Question 
First of all we start by POST ORDER
then we replace node's right by nodes left and then traverse 
to last right element and then attach the previous right to it's right.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is not None:
            self.flatten(root.left)
            self.flatten(root.right)
            right = root.right
            root.right = root.left
            root.left = None
            while root.right:
                root = root.right
            root.right = right
