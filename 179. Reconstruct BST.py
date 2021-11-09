# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    return None




# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

		
		
#     def insert(self, value):
#         currentNode = self
		
#         while True:
#             if value<currentNode.value:
#                 if currentNode.left is None:
#                     currentNode.left = BST(value)
#                     break
#                 else:
#                     currentNode = currentNode.left
#             else:
#                 if currentNode.right is None:
#                     currentNode.right = BST(value)
#                     break
#                 else:
#                     currentNode = currentNode.right
#         # Do not edit the return statement of this method.
#         return self


# preOrderTraversal = [10, 4, 2, 1, 5, 17, 19, 18]
# def reconstructBst(preOrderTraversal):
#     # Write your code here.
#     return None