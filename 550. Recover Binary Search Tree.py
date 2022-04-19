"""
Find the node which disobeys the BSt properties 
Then check is swapping left would yield correct ans if not
swap right, since we know that exactly 2 nodes were swapped 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first, self.second, self.prevNode = None, None, None
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inOrder(self, root):
        if not root:
            return

        self.inOrder(root.left)
        if self.prevNode and self.prevNode.val > root.val:
            if not self.first:
                self.first = self.prevNode
            self.second = root
        self.prevNode = root
        self.inOrder(root.right)
