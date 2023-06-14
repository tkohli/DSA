# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = float("inf")
        self.prev = float("inf")

        def dfs(node):
            if node:
                dfs(node.left)
                if self.prev != float("inf"):
                    self.ans = min(abs(node.val - self.prev), self.ans)
                self.prev = node.val
                dfs(node.right)

        dfs(root)
        return self.ans
