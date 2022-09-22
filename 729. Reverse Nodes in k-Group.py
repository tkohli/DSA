# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        We start by creating a dummyHead as we have to reverse even head
        then take count and and for every K group do reverse
        Actually tougher than it seems  
        """
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        cur, prev, next = dummyNode, dummyNode, dummyNode
        cnt = 0
        while cur.next:
            cnt += 1
            cur = cur.next
        while cnt >= k:
            cur = new = prev.next
            next = cur.next
            for _ in range(k-1):
                tmp = next.next
                next.next = cur
                cur = next
                next = tmp

            prev.next = cur
            new.next = next
            prev = new
            cnt -= k
        return dummyNode.next
