# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
	p1prev = None
	p2 = headTwo
	while p1 is not None and p2 is not None:
		if p1.value < p2.value:
			p1prev = p1
			p1 = p1.next
		else:
			if p1prev is not None:
				p1prev.next = p2
			p1prev = p2
			p2 = p2.next
			p1prev.next = p1
	if p1 is None:
		p1prev.next = p2
	return headOne if headOne.value < headTwo.value else headTwo
