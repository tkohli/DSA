intersectVal = 8
listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]
skipA = 2
skipB = 3
"""
intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, listA: ListNode, listB: ListNode) -> Optional[ListNode]:

        if listA is None or listB is None:
            return None

        n1 = listA
        n2 = listB
        while n1 != n2:
            if n1 is None:
                n1 = listB
            else:
                n1 = n1.next
            if n2 is None:
                n2 = listA
            else:
                n2 = n2.next
        return n1
