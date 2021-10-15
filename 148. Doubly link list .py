# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        self.insertBefore(self.head,node)


    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return 
        self.insertAfter(self.tail,node)


    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return # No operation needed 
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            #dealing with head
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert


    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return # No operation needed 
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            #dealing with tail
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert


    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
        # traverse the linked list
        node = self.head
        currentIdx = 1
        while node is not None and currentIdx != position:
            node = node.next
            currentIdx += 1
        if node is not None:
            self.insertBefore(node,nodeToInsert)
        else:
            self.setTail(nodeToInsert)


    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node # we need to take a record of pointers as we remove an binding will be lost
            node = node.next 
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
       

    def remove(self, node):
        # check if node is head or tail
        if (node == self.head):
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev 
        # Now we want to remove the binding from element so that we can remove it
        self.removeNodeBindings(node)


    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
        # while node.value:
        #     if node.value == value:
        #         return True
        #     node = node.next
        # return False


    def removeNodeBindings(self,node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None