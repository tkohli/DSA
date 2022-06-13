# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sums = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int, lst=[], sum=0) -> List[List[int]]:
        if root:
            if root.left is None and root.right is None and sum+root.val == targetSum:
                self.sums.append(lst+[root.val])
            self.pathSum(root.left, targetSum, lst+[root.val], sum+root.val)
            self.pathSum(root.right, targetSum, lst+[root.val], sum+root.val)
        return self.sums
