# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    """
    Start with DFS
    Find height of tree and then count nodes
    """


    # Write your code here.
    return -1

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0)
        


class TreeInfo:
    def __init__(self,diameter,height):
        self.diameter = diameter
        self.height = height