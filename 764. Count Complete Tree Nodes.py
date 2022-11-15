# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        T(n) = T(n/2) + log(n) , log(n) is the height part,T(n/2) is the recursion part. So T(n) = T(n/4) + 
        log(n/2)+log(n) =T(n/8)+log(n/4)+log(n/2)+log(n).....etc. If we add up all the log(n/numerator), there are 
        log(n) factors , the result should be log(n)*log(n)
        
        If left sub tree height equals right sub tree height then,
        a. left sub tree is perfect binary tree
        b. right sub tree is complete binary tree
        If left sub tree height greater than right sub tree height then,
        a. left sub tree is complete binary tree
        b. right sub tree is perfect binary tree
        """
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)
        
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
    
        
        # if root is None:
        #     return 0
        # return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
#         self.count = 0
#         def helper(node):
#             self.count+=1
#             if node.left:
#                 helper(node.left)
#             if node.right:
#                 helper(node.right)
        
#         helper(root)
#         return self.count