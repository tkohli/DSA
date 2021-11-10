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
    return getTreeInfo(tree).diameter

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0,0)
    leftTreeinfo = getTreeInfo(tree.left)
    rightTreeinfo = getTreeInfo(tree.right)
    longestPathThroughRoot = leftTreeinfo.height + rightTreeinfo.height
    maxDiameterTilNow = max(leftTreeinfo.diameter,rightTreeinfo.diameter)
    currentDiameter = max(longestPathThroughRoot,maxDiameterTilNow)
    currentHeight =1+ max(leftTreeinfo.height,rightTreeinfo.height) 
    return TreeInfo(currentDiameter,currentHeight)


class TreeInfo:
    def __init__(self,diameter,height):
        self.diameter = diameter
        self.height = height