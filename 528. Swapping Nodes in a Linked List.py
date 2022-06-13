# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = None
        i = 1
        j = -k
        node = head
        tmp = head
        while node:
            if i == k:
                start = node
            if j >= 0:
                tmp = tmp.next
            i += 1
            j += 1
            node = node.next
        start.val, tmp.val = tmp.val, start.val
        return head
