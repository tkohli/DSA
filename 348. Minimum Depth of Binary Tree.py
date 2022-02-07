# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minHeight = float("inf")

    def minDepth(self, root: Optional[TreeNode], depth=1) -> int:
        if root:
            if root.left is None and root.right is None:
                self.minHeight = min(self.minHeight, depth)
            else:
                self.minDepth(root.left, depth+1)
                self.minDepth(root.right, depth+1)

        return self.minHeight if self.minHeight != float("inf") else 0


# Better way
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth = depth + 1
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left == None and node.right == None:
                    return depth
                elif node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return -1
