# root = [4,8,5,0,1,null,6]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        """
        So here we will start with some dfs and work our way up by keeping the avg 
        value of node. small dfs
        """
        self.count = 0

        def dfs(node):
            if not node:
                return 0
            avg = node.val
            ele = 1
            if node.left:
                a, e = dfs(node.left)
                ele += e
                avg += a
            if node.right:
                a, e = dfs(node.right)
                ele += e
                avg += a
            cur = avg//ele
            if cur == node.val:
                self.count += 1

            return avg, ele

        dfs(root)
        return self.count
