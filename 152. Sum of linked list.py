# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # We need a new linkedlist and then keep track of carry numbers to add uint places 
    NewLinkedList = LinkedList(0)
    currentNode = NewLinkedList
    carry = 0
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo
    while nodeOne is not None or nodeTwo is not None or carry!=0:
        firstValue = nodeOne.value if nodeOne is not None else 0
        secondValue = nodeTwo.value if nodeTwo is not None else 0
        sumOfValue = firstValue+secondValue+carry
        newValue = sumOfValue%10
        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode = newNode
		carry = sumOfValue//10
        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None
	return NewLinkedList.next