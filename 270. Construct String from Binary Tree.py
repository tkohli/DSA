# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)+""
        if root.right is None:
            return str(root.val)+"("+str(self.tree2str(root.left))+")"
        return str(root.val)+"("+str(self.tree2str(root.left))+")("+str(self.tree2str(root.right))+")"
