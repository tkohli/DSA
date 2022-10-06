# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        def addRow(node, d):
            if not node:
                return
            if d == depth - 1:
                left, right = node.left, node.right
                node.left = TreeNode(val, left=left)
                node.right = TreeNode(val, right=right)
                return
            addRow(node.left, d+1)
            addRow(node.right, d+1)
        addRow(root, 1)
        return root


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # traverse level by level if I reach depth - 1
        # then add the values to the childrens
        if depth == 1:
            return TreeNode(val=val, left=root)
        q = deque([root])
        cur_level = 1
        while q:

            for i in range(len(q)):
                cur_node = q.popleft()
                if depth - 1 == cur_level:
                    l_child, r_child = cur_node.left, cur_node.right
                    l_new, r_new = TreeNode(val=val, left=l_child), TreeNode(
                        val=val, right=r_child)
                    cur_node.left, cur_node.right = l_new, r_new

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

            cur_level += 1
        return root
