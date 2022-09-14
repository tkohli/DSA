# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.num_pseudo_palindromic = 0

        def is_pseudo_palindromic(path: dict) -> bool:
            one_odd = False
            for count in path.values():
                if count % 2 == 1:
                    if one_odd:
                        return False
                    one_odd = True
            return True

        def helper(node: Optional[TreeNode], path: dict):
            if node:
                path[node.val] += 1
                if not node.left and not node.right:
                    if is_pseudo_palindromic(path):
                        self.num_pseudo_palindromic += 1
                helper(node.left, path)
                helper(node.right, path)
                path[node.val] -= 1
        helper(root, defaultdict(int))
        return self.num_pseudo_palindromic
