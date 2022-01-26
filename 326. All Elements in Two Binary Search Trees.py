# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            self.arr.append(node.val)
            self.inOrder(node.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.inOrder(root1)
        self.inOrder(root2)
        self.arr.sort()
        return self.arr
