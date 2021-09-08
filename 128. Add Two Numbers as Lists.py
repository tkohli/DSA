# Add Two Numbers as Lists
"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list

So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
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
	def addTwoNumbers(self, A, B):
        def addTwoNumbers(self, A, B):
        lst1 = []
        lst2 = []
        while A:
            lst1.append(A.val)
            A = A.next
        while B:
            lst2.append(B.val)
            B = B.next
        lst1.reverse()
        lst2.reverse()
        val1 = ""
        val2 = ""
        for v in lst1:
            val1 += str(v)
        for v in lst2:
            val2 += str(v)
        val = str(int(val1) + int(val2))
        lst = []
        for e in val:
            lst.append(e)
        head = ListNode('root')
        root = head
        lst.reverse()
        for ele in lst:
            h = ListNode(ele)
            head.next = h
            head = head.next
        return root.next