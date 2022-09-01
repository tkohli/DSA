# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def find(node, currMax):

            if node.val >= currMax:
                currMax = max(node.val, currMax)
                self.count += 1

            if node.left:
                find(node.left, currMax)
            if node.right:
                find(node.right, currMax)

        find(root, float("-inf"))
        return self.count


#         ans = 0
#         q = deque()

#         q.append((root,-inf))
#         '''perform bfs  with track of maxval till perant node'''

#         while q:
#             node,maxval = q.popleft()
#             if node.val >= maxval:
#                 ans += 1

#             if node.left:    #new max update
#                 q.append((node.left,max(maxval,node.val)))

#             if node.right:
#                 q.append((node.right,max(maxval,node.val)))

#         return ans
