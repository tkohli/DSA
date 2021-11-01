class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self,newValue):
        if self.value:
            if self.value<newValue:
                if self.right is None:
                    self.right = node(newValue)
                else:
                    self.right.insert(newValue)
            else:
                if self.left is None:
                    self.left = node(newValue)
                else:
                    self.left.insert(newValue)
        else:
            self.value = newValue

            
    def findVal(self,findValue):
        if findValue > self.value:
            if self.right: # if self.right is not none
                return self.right.findVal(findValue)
            return False
        elif findValue < self.value:
            if self.left:
                return self.left.findVal(findValue)
            return False
        else:
            return True

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value)
        if self.right:
            self.right.printTree()


root = node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)


root.printTree()
print(root.findVal(35))
# Todo Remove an element in BST