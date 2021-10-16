# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	# find the total length of linkedList
	node = head
	count = 0
	while node is not None:
		count+=1
		node = node.next
	target = (count - k)
	print(target)
	node = head
	count = 1
	while node is not None:
		if target == 0:
			head.value = head.next.value
			head.next = head.next.next
			break
		elif count == target:
			node.next = node.next.next
			break
		count+=1
		node = node.next
	return head
	
		
