# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        h = head
        while h.next:
            if h.next.val == val:
                h.next = h.next.next
            else:
                h = h.next
        while head and head.val == val:
            head = head.next
        return head
