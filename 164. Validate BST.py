# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return helperValidateBST(tree,float('-inf'),float('inf'))

def helperValidateBST(tree,minValue,maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    isLeftValid = helperValidateBST(tree.left,minValue,tree.value)
    return isLeftValid and helperValidateBST(tree.right,tree.value,maxValue)