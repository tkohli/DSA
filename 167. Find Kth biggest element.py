# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    out = []
    array = inOrderTraversal(tree,out)# Write your code here.
    return out[len(array)-k]

def inOrderTraversal(tree,array):
    if tree:
        inOrderTraversal(tree.left,array)
        array.append(tree.value)
        inOrderTraversal(tree.right,array)
    return array