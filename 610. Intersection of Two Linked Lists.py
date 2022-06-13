"""
For naive solution we can use a hashSet and then keep track of same val 
while looping in second list

Optimization -> We take lst1 as n and n2 for lst2 then we do cycling check which 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

        # if headA is None and headB is None:
        #     return None

        # n = headA
        # m = headB

        # while n != m:
        #     if n is None:
        #         n = headB
        #     else:
        #         n = n.next
        #     if m is None:
        #         m = headA
        #     else:
        #         m = m.next
        # return n
