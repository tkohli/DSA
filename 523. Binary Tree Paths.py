# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def binaryTreePaths(self, root: Optional[TreeNode], lst='') -> List[str]:
        if root:
            if root.left is None and root.right is None:
                self.ans.append(lst+str(root.val))
            self.binaryTreePaths(root.left, lst + str(root.val) + '->')
            self.binaryTreePaths(root.right, lst + str(root.val) + '->')
        return self.ans
