# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    inOrderNode = getNodesInOrder(root, [])
    for i in range(0, len(inOrderNode)-1):
        leftNode = inOrderNode[i]
        rightNode = inOrderNode[i+1]
        leftNode.right = rightNode
        rightNode.left = leftNode
    return inOrderNode[0]


def getNodesInOrder(tree, array):
    if tree is not None:
        getNodesInOrder(tree.left, array)
        array.append(tree)
        getNodesInOrder(tree.right, array)
    return array
