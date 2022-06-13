# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sums = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, sum=0) -> bool:
        if root and not self.sums:
            if root.left is None and root.right is None:
                if sum+root.val == targetSum:
                    self.sums = True
            self.hasPathSum(root.left, targetSum, sum+root.val)
            self.hasPathSum(root.right, targetSum, sum+root.val)
        return self.sums
