# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# traverse with relink
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrder(node):
            if node:
                inOrder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inOrder(node.right)

        ans = self.cur = TreeNode(None)
        inOrder(root)
        return ans.right
