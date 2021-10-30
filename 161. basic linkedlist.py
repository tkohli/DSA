class Node:
    def _init_(self,value):
        self.value = value
        self.next = None

class Linkedlist:
    def _init_(self):
        self.head = None

    def insert(self,valueInsert):
        if self.head ==None:
            self.head =Node(valueInsert)
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next=Node(valueInsert)

    def printlist(self):
        node = self.head
        while node is not None:
            print(node.value)
            node =node.next

ll = Linkedlist()
ll.insert(1)
ll.insert(40)
ll.printlist()