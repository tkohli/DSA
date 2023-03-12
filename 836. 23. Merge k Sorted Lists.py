from typing import List,Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0
        for node in lists:
            if node:
                count += 1
                heapq.heappush(heap, (node.val, count, node))
        dummy = ListNode(0)
        cur = dummy
        while heap:
            _, _, tmp = heapq.heappop(heap)
            cur.next = tmp
            cur = tmp
            if tmp.next:
                count+=1
                heapq.heappush(heap, (tmp.next.val, count, tmp.next))
        
        return dummy.next
        