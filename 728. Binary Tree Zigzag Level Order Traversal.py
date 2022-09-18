# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# proper usage of DSA Smart solution
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        even_level = False
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                if even_level:
                    # pop from right and append from left.
                    node = queue.pop()
                    # to maintain the order of nodes in the format of [left, right, left, right]
                    # we push right first since we are appending from left
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                else:
                    # pop from left and append from right
                    node = queue.popleft()
                    # here the order is maintained in the format [left, right, left, right]
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                level.append(node.val)
            res.append(level)
            even_level = not even_level
        return res


"""
this is such a simple approach just reverse all odd level then append it :) cheat but works 
"""


class Solution:
    def zigzagLevelOrder(self, root):
        queue = collections.deque([root])
        res = []
        while queue:
            r = []
            for _ in range(len(queue)):
                q = queue.popleft()
                if q:
                    r.append(q.val)
                    queue.append(q.left)
                    queue.append(q.right)
            r = r[::-1] if len(res) % 2 else r
            if r:
                res.append(r)
        return res
