# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    mutate(root, None, None)
    return root


def mutate(node, parentNode, isLeftNode):
    if node is None:
        return
    left, right = node.left, node.right
    # change left node
    mutate(left, node, True)
    if parentNode is None:
        node.right = None
    elif isLeftNode:
        node.right = parentNode.right
    else:
        if parentNode.right is None:
            node.right = None
        else:
            node.right = parentNode.right.left
    mutate(right, node, False)
