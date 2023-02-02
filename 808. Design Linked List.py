# Design Linked List
class Node:
    def __init__ (self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def get(self, index: int) -> int:
        i=0
        n = self.head
        while n:
            if i==index:
                return n.val
            i+=1
            n= n.next
            # print(n.val)
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return    
        tmp = self.head
        self.head = Node(val)
        self.head.next = tmp
        

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return None
        n = self.head
        while n.next :
            n = n.next
        n.next = Node(val)
         

    def addAtIndex(self, index: int, val: int) -> None:
        if self.head is None and index!=0:
            return None
        if index==0:
            self.addAtHead(val)
            return None
        newNode = Node(val)
        i=1
        prev = self.head
        n = self.head.next
        while n is not None:
            if i==index:
                prev.next = newNode
                newNode.next = n
            i+=1
            n = n.next
            prev = prev.next
        if i==index:
            prev.next = newNode
            newNode.next = n

            
    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return None
        if index == 0:
            self.head = self.head.next
            return
        i=1
        prev = self.head
        n = self.head.next
        while n is not None:
            if i==index:
                prev.next = n.next
            i+=1
            prev = prev.next
            n = n.next

        

# myLinkedList = MyLinkedList()
# myLinkedList.addAtHead(7)
# myLinkedList.addAtHead(2)
# myLinkedList.addAtHead(1)
# myLinkedList.addAtIndex(3, 0)              
# myLinkedList.deleteAtIndex(2)
# myLinkedList.addAtHead(6)
# myLinkedList.addAtTail(4)
# print(myLinkedList.get(4))
# myLinkedList.addAtHead(4)
# myLinkedList.addAtIndex(5, 0)  
# myLinkedList.addAtHead(6)
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)