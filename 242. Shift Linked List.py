# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    """
    New head and new tail so that rest of all things remains same 
    """
    # count and find tail
    listTail = head
    listLen = 1
    while listTail.next is not None:
        listLen += 1
        listTail = listTail.next
    # Check position
    offset = abs(k) % listLen
    if offset == 0:
        return head
    newTailPosition = listLen-offset if k > 0 else offset
    # NewTail
    newTail = head
    for i in range(1, newTailPosition):
        newTail = newTail.next
    newhead = newTail.next
    newTail.next = None
    listTail.next = head
    return newhead
