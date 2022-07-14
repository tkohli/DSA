# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        The below code is slicing and searching so we find ways to avoid both of these
        https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/Figures/105/105-Page-2.png
        """
        preOrderIndex = 0
        inOrderIndexMap = {}
        for idx, ele in enumerate(inorder):
            inOrderIndexMap[ele] = idx

        def helper(left, right):
            nonlocal preOrderIndex
            if left > right:
                return None
            rootValue = preorder[preOrderIndex]
            root = TreeNode(rootValue)
            preOrderIndex += 1
            root.left = helper(left, inOrderIndexMap[rootValue]-1)
            root.right = helper(inOrderIndexMap[rootValue]+1, right)
            return root

        return helper(0, len(inorder)-1)

    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if preorder == [] or inorder == []:
    #         return None
    #     # lNR inOrder preOrder NLR
    #     root = TreeNode(preorder[0])
    #     mid = inorder.index(preorder[0])
    #     root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
    #     root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
    #     return root
