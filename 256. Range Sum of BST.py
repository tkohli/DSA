# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root is None:
            return
        if root.val >= low and root.val <= high:
            print(root.val)
            self.sum += root.val
        if root.left is not None:
            self.rangeSumBST(root.left, low, high)
        if root.right is not None:
            self.rangeSumBST(root.right, low, high)

        return self.sum
