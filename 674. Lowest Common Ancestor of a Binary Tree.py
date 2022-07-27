"""
Approach 1: Recursive Approach
Intuition

The approach is pretty intuitive. Traverse the tree in a depth first manner. 
The moment you encounter either of the nodes p or q, return some boolean flag. 
The flag helps to determine if we found the required nodes in any of the paths. 
The least common ancestor would then be the node for which both the subtree 
recursions return a True flag. It can also be the node which itself is one of 
p or q and for which one of the subtree recursions returns a True flag.

Let us look at the formal algorithm based on this idea.

Algorithm

Start traversing the tree from the root node.

If the current node itself is one of p or q, we would mark a variable mid as 
True and continue the search for the other node in the left and right branches.

If either of the left or the right branch returns True, this means one of the 
two nodes was found below.

If at any point in the traversal, any two of the three flags left, right or 
mid become True, this means we have found the lowest common ancestor for the 
nodes p and q.
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recursiveHelper(currentNode):
            if not currentNode:
                return False

            left = recursiveHelper(currentNode.left)
            right = recursiveHelper(currentNode.right)

            mid = currentNode == p or currentNode == q

            if left+right+mid >= 2:
                self.ans = currentNode

            return mid or left or right

        recursiveHelper(root)
        return self.ans


"""
Approach 2: Iterative using parent pointers
Intuition

If we have parent pointers for each node we can traverse back from p and q to get their ancestors. 
The first common node we get during this traversal would be the LCA node. We can save the parent 
pointers in a dictionary as we traverse the tree.

Algorithm
Start from the root node and traverse the tree.

Until we find p and q both, keep storing the parent pointers in a dictionary.

Once we have found both p and q, we get all the ancestors for p using the parent 
dictionary and add to a set called ancestors.

Similarly, we traverse through ancestors for node q. If the ancestor is present 
in the ancestors set for p, this means this is the first ancestor common between p and q (while traversing upwards) and hence this is the LCA node.

For more variation we can store parent value in our tree node
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]
        while q not in ancestor:
            q = parent[q]
        return q
