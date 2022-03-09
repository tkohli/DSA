"""
Perform insertion sort on a linked list.
The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
"""
# Definition for singly-linked list.
import re


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev, cur = head, head.next
        
        while cur:
            if cur.val >= prev.val:
                prev, cur = cur, cur.next
                continue
                
            tmp = dummy
            while cur.val > tmp.next.val:
                tmp = tmp.next

            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next
        return dummy.next