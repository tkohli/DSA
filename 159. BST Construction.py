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

    def remove(self,value,parentNode = None):
        if value<self.value:
            if self.value is not None:
                self.left.remove(value,self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value,self)
        # now we are at the value
        else:
            if self.left is not None and self.right is not None:
                # Now we need to find min of this sub tree
                self.value = self.right.getMinValue()
                self.right.remove(self.value,self)
            elif parentNode is not None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass # Last Node or no child 
            elif parentNode.left == self:
                parentNode.left = self.left if self.left is not None else self.right
            elif parentNode.right == self:
                parentNode.right = self.left if self.left is not None else self.right
        return self

    
    def getMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinValue()
            
root = node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.remove(35)

root.printTree()
print(root.findVal(35))
# Todo Remove an element in BST