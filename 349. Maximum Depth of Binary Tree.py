# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth = depth + 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left == None and node.right == None:
                    continue
                elif node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
