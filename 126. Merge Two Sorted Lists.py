# Merge Two Sorted Lists
"""
Merge two sorted linked lists and return it as a new list. 

The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

For example, given following linked lists :

  5 -> 8 -> 20 
  4 -> 11 -> 15
The merged list should be :

4 -> 5 -> 8 -> 11 -> 15 -> 20
"""
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
        head = ListNode('root')
        root = head
        while A is not None and B is not None:
            if A.val <= B.val:
                root.next = A
                A = A.next
            else:
                root.next = B
                B = B.next
            root = root.next
        
        if A is not None:
            root.next = A
        if B is not None:
            root.next = B
            
        return head.next
        # if A.val < B.val:
        #     head = A
        # else:
        #     head = B
        # while A.next!= None and B.next != None:
        #     if A.val > B.val:
        #         A.next = B
        #         A = B.next
        #     else:
        #         B.next = A
        #         B = A.next
                
        # return head