# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        self.isBST = True

        def BST(root, left, right):
            if root:
                if root.val <= left or root.val >= right:
                    self.isBST = False
                    return
                BST(root.left, left, root.val)
                BST(root.right, root.val, right)
        BST(root, float("-inf"), float("inf"))
        return self.isBST
        """
        :type root: TreeNode
        :rtype: bool
        """
        # if root is not None:
        #     if root.left and root.right:
        #         if root.left.val<root.val and root.right.val>root.val:
        #             self.isValidBST(root.left)
        #             self.isValidBST(root.right)
        #         else:
        #             self.BST =  False
        #     elif root.left:
        #         if root.left.val < root.val:
        #             self.isValidBST(root.left)
        #         else:
        #             self.BST = False
        #     elif root.right:
        #         if root.right.val > root.val:
        #             self.isValidBST(root.right)
        #         else:
        #             self.BST = False
        # return self.BST
