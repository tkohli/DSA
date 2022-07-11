"""
Right Side View of Binary Tree 
for this we have to do a reverse traversal 
in which we start from node,right,left
also keeping the track of their depth so 
that we add only new and visible elements 
from our binary tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def helper(node, depth):
            if node:
                if depth == len(ans):
                    ans.append(node.val)
                helper(node.right, depth+1)
                helper(node.left, depth+1)

        ans = []
        helper(root, 0)
        return ans

# we can also use 2 queues for the same


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            ans.append(queue[-1].val)
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        return ans
