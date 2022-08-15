# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        For this question we do not need to keep track of parent node as this
        is BST so if find value such that left<=val and right >= val
        So we return that node
        We need to find which value goes to left and right as it is not 
        stated that which value is bigger ir smaller 
        """
        left = p.val if p.val < q.val else q.val
        right = p.val if p.val > q.val else q.val
        while root is not None:
            if left <= root.val and root.val >= right:
                return root
            elif root.val > left and root.val > right:
                root = root.right
            else:
                root = root.left
