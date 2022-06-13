# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, o: TreeNode, c: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = None

        def inOrder(node, cnode):
            if node and self.ans is None:
                inOrder(node.left, cnode.left)
                if node == target:
                    self.ans = cnode
                inOrder(node.right, cnode.right)

        inOrder(o, c)
        return self.ans
