# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level = 1
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            value = []
            for i in range(len(queue)):
                if level%2==0:
                    node = queue.pop()
                    value.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                    
                else:
                    node = queue.popleft()
                    value.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            ans.append(value)
            level+=1

        return ans



        # if root is None:
        #     return []
        # ans = []
        # level = 1
        # queue = [root]
        # while queue:
        #     tmp = []
        #     value = []
        #     for node in queue:
        #         value.append(node.val)
        #         if node.left:
        #             tmp.append(node.left)
        #         if node.right:
        #             tmp.append(node.right)
            
        #     queue = tmp[:]
        #     if level%2==0:
        #         ans.append(value[::-1])
        #     else:
        #         ans.append(value)
        #     level+=1

        # return ans
