# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        temp = ListNode(0)
        curr = temp
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            num = y+x+carry
            carry = num//10
            num = num % 10
            curr.next = ListNode(num)
            curr = curr.next
            l1 = l1.next if l1 else False
            l2 = l2.next if l2 else False
        if carry:
            curr.next = ListNode(carry)
        return temp.next
