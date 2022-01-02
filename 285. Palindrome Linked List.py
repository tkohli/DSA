# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        secondHead = prev
        firstHead = head
        while secondHead:
            if secondHead.val != firstHead.val:
                return False
            secondHead = secondHead.next
            firstHead = firstHead.next
        return True
