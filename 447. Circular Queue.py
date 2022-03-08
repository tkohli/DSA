"""
We can don this in both array and LL
but let's use LL to improve everything
We are given size k
Implementation the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.

Use a doubly linkedList it would be more helpful
"""

class ListNode:
    def __init__(self, val, nxt, prev):
        self.val = val
        self.next = nxt
        self.prev = prev 


class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0,None,None)
        self.right = ListNode(0,None,self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curNode = ListNode(value,self.right,self.right.prev)
        self.right.prev.next = curNode
        self.right.prev = curNode
        space-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space+=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next==self.right

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()