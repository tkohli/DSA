# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # first edge cases
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        nodeOne = list1
        nodeTwo = list2
        prev = None
        while nodeOne and nodeTwo:
            if nodeOne.val < nodeTwo.val:
                prev = nodeOne
                # prev.next = nodeTwo
                nodeOne = nodeOne.next
            else:
                if prev: # i.e. nodeOne was smaller
                    prev.next = nodeTwo
                prev = nodeTwo
                nodeTwo = nodeTwo.next
                prev.next = nodeOne

        if nodeOne is None:
            prev.next = nodeTwo

        if list1.val<list2.val:
            return list1
        else:
            return list2
