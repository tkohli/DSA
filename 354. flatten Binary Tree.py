# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root)
    return leftMost


def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubTreeLeftMost, leftSubTreeRightMost = flattenTree(node.left)
        connectNode(leftSubTreeRightMost, node)
        leftMost = leftSubTreeLeftMost
    if node.right is None:
        rightMost = node
    else:
        rightSubTreeLeftMost, rightSubTreeRightMost = flattenTree(node.right)
        connectNode(node, rightSubTreeLeftMost)
        rightMost = rightSubTreeRightMost
    return [leftMost, rightMost]


def connectNode(left, right):
    left.right = right
    right.left = left
