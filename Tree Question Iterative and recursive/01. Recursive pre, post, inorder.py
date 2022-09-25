# all these code run in
# O(n) Time | O(n) Space  -> Logically we can say that O(h) Space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.arr = []
        self.arr1 = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.arr.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.arr

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.arr1.append(root.val)
        return self.arr

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            self.inorderTraversal(root.right)
            self.arr2.append(root.val)
        self.arr = []
        return self.arr
