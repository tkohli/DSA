"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of 
two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is 
defined between two nodes p and q as the lowest node in T that has 
both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        left = p.val if p.val < q.val else q.val
        right = p.val if p.val > q.val else q.val
        while root is not None:
            val = root.val
            if left <= val and right >= val:
                return root
            elif val < right and val < left:
                root = root.right
            else:
                root = root.left
