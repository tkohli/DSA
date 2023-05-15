# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        end = head
        start = head
        i = 1
        tmp = head
        while tmp:
            if i==k:
                start = tmp
            if k<i:
                end = end.next
            i+=1
            tmp = tmp.next
        start.val,end.val = end.val,start.val
        return head