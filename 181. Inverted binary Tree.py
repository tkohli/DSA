def invertBinaryTree(tree):
    if tree is None:
        return
    swap(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

    # queue = [tree] # we will pop 0 :)
    # while queue:
    #     current = queue.pop(0)
    #     if current is None:
    #         pass
    #     swap(current)
    #     queue.append(tree.left)
    #     queue.append(tree.right)

def swap(node):
    node.left,node.right = node.right,node.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
