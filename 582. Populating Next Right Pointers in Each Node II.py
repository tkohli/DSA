"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def findNext(node):
            if node is None:
                return None
            if node.left:
                return node.left
            if node.right:
                return node.right
            return findNext(node.next)

        def helper(root):
            if root is None:
                return None
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    root.left.next = findNext(root.next)
            if root.right:
                root.right.next = findNext(root.next)
            helper(root.right)
            helper(root.left)
        helper(root)
        return root
