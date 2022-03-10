# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newList = ListNode(0)
        tmp = newList
        while l1 or l2 or carry:
            if l1 is None:
                i = 0
            else:
                i = l1.val
            if l2 is None:
                j = 0
            else:
                j = l2.val
            s = i+j+carry
            carry = s//10
            s = s%10
            tmp.next = ListNode(s)
            tmp = tmp.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return newList.next