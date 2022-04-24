# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        cur, prev = head, dummyHead
        for i in range(left-1):
            cur = cur.next
            prev = prev.next

        for i in range(right-left):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp

        return dummyHead.next
