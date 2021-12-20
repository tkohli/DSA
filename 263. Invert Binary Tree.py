# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invert(self, root):
        if root is not None:
            root.left, root.right = root.right, root.left

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            self.invert(root)
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
