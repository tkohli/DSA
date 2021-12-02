# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class getTreeInfo:
    def __init__(self,isBalanced,height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    TreeInfo = getTreeinfo(tree)
    return TreeInfo.isBalanced


def getTreeinfo(node):
    # Know balanced and height
    if node == None:
        return getTreeInfo(True,-1)
    leftSubtreeInfo = getTreeinfo(node.left)
    rightSubtreeInfo = getTreeinfo(node.right)

    #check balanced tree or not
    isBalanced = leftSubtreeInfo.isBalanced and rightSubtreeInfo.isBalanced and abs(
        leftSubtreeInfo.height-rightSubtreeInfo.height) <= 1
    height = max(leftSubtreeInfo.height,rightSubtreeInfo.height)+1
    return getTreeInfo(isBalanced,height)