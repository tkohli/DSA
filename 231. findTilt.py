# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def __init__(self):
        self.totaltilt = 0
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return  self.totaltilt
    
    
    def dfs(self,node):
        if node is None:
            return 0
        leftsum= self.dfs(node.left)
        rightsum= self.dfs(node.right)
        tilt = abs(leftsum-rightsum)
        self.totaltilt+=tilt
        return node.val+leftsum+rightsum
   