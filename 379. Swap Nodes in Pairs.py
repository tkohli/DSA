# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempNode = ListNode(0)
        tempNode.next = head
        prevNode = tempNode
        while prevNode.next and prevNode.next.next:
            sec = prevNode.next.next
            first = prevNode.next
            first.next = sec.next
            sec.next = first
            prevNode.next = sec
            prevNode = first

        return tempNode.next
