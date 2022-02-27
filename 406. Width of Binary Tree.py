# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = [[root, 1]]
        maxWidth = 0
        while q:
            # find the difference for upcomming queue
            maxWidth = max(maxWidth, q[-1][1] - q[0][1] + 1)
            for _ in range(len(q)):
                curr, idx = q.pop(0)
                if curr.left:
                    q.append([curr.left, idx*2])
                if curr.right:
                    q.append([curr.right, idx*2+1])
        return maxWidth
