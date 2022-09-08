# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        stack = []
        q = deque([root])
        while q:
            item = q.pop()
            if item == ')':
                stack.append(item)
                continue

            stack.extend(['(', str(item.val)])
            if not item.left and item.right:
                stack.append('()')

            if item.right:
                q.extend([')', item.right])

            if item.left:
                q.extend([')', item.left])

        return ''.join(stack[1:])

        # if root is None:
        #     return ""
        # elif root.left is None and root.right is None:
        #     return str(root.val)
        # elif root.right is None:
        #     return str(root.val)+"("+self.tree2str(root.left)+")"
        # return str(root.val)+"("+self.tree2str(root.left)+")("+self.tree2str(root.right)+")"
