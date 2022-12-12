# Invert Binary Tree

"""
    Iterative Solution
    using Queue initailly having root node then for current value pop node from queue
    after that swap left node and right node of the current node and append these node 
    to queue and do this repeatly until we find a empty queue.

          Binary Tree                         Invert Binary Tree 

                5                                    5
            ----------                          -----------
            4         8                         8         4
            
       --------     --------               --------     --------
       7     -2    -1      9               9     -1     -2     7

"""

# Time Complexity = O(n) || Space Complexity = O(n)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        """
        if this was not a binary tree then we would have an array of children
        """
        self.val = val
        self.left = left
        self.right = right


node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(7)
node5 = TreeNode(-2)
node6 = TreeNode(-1)
node7 = TreeNode(9)


tree = node1
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node7
node3.left = node6


def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        current.left, current.right = current.right, current.left
        queue.append(current.left)
        queue.append(current.right)


def display(tree):
    if tree is not None:
        print(tree.val)
        display(tree.left)
        display(tree.right)


invertBinaryTree(tree)
display(tree)
