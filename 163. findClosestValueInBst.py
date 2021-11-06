def findClosestValueInBst(tree, target):
    currentNode = tree
    closest = tree.value
    while currentNode is not None:
        if abs(target-closest) > abs(target-currentNode.value):
            closest = currentNode.value
        if target > currentNode.value:
            currentNode = currentNode.right
        elif target < currentNode.value:
            currentNode = currentNode.left
        else:
            break 
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
