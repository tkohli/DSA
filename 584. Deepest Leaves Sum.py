# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.maxDepth = 1
        self.leafSum = 0

    def depth(self, node, d):
        if node is None:
            return
        if d > self.maxDepth:
            self.maxDepth = d
            self.leafSum = node.val
        elif d == self.maxDepth:
            self.leafSum += node.val
        self.depth(node.left, d+1)
        self.depth(node.right, d+1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.depth(root, 1)
        return self.leafSum
