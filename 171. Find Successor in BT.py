# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
	array = inOrderTraversal(tree)
	idx = 1
	for arr in array:
		if arr == node:
			return array[idx]
		if idx == len(array)-1:
			return None
		idx+=1

def inOrderTraversal(root,array=[]):
	if root is None:
		return array
	inOrderTraversal(root.left,array)
	array.append(root)
	inOrderTraversal(root.right,array)
	return array