class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def printTree(self):
        print(self.value)

root = node(27)
root.printTree()