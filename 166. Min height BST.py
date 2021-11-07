def minHeightBst(array):
    return binaryBSTConst(array, 0, len(array)-1)


def binaryBSTConst(array,startIdx,endIdx):
    if endIdx < startIdx:
        return None
    mid = (startIdx+endIdx)//2
    bst = BST(array[mid])
    bst.left = binaryBSTConst(array,startIdx,mid-1)
    bst.right = binaryBSTConst(array,mid+1,endIdx)
    return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
