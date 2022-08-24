# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        slow = fast = node
        while fast and fast.next:  # is not None
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        h1 = head
        h2 = prev

        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next

        return True
