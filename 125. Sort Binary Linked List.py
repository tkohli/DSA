# Sort Binary Linked List
"""
Problem Description

Given a Linked List A consisting of N nodes.

The Linked List is binary i.e data values in the linked list nodes consist of only 0's and 1's.

You need to sort the linked list and return the new linked list.

NOTE:

Try to do it in constant space.


Problem Constraints
 1 <= N <= 105

 A.val = 0 or A.val = 1



Input Format
First and only argument is the head pointer of the linkedlist A.



Output Format
Return the head pointer of the new sorted linked list.



Example Input
Input 1:

 1 -> 0 -> 0 -> 1
Input 2:

 0 -> 0 -> 1 -> 1 -> 0


Example Output
Output 1:

 0 -> 0 -> 1 -> 1
Output 2:

 0 -> 0 -> 0 -> 1 -> 1


Example Explanation
Explanation 1:

 The sorted linked list looks like:
  0 -> 0 -> 1 -> 1
Explanation 2:

 The sorted linked list looks like:
  0 -> 0 -> 0 -> 1 -> 1
"""
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        node = A
        count = [0, 0]

        while node is not None:
            count[node.val] += 1
            node = node.next

        node = A

        for i in range(count[0]):
            node.val = 0
            node = node.next

        for i in range(count[1]):
            node.val = 1
            node = node.next

        return A
# # Definition for singly-linked list.
# # class ListNode:
# #    def __init__(self, x):
# #        self.val = x
# #        self.next = None

# class Solution:
#     # @param A : head node of linked list
#     # @return the head node in the linked list
#     def solve(self, A):
#         temp = A
#         ones = 0
#         zeros = 0
#         while temp.next != None:
#             if temp.val == 1:
#                 ones += 1
#             if temp.val == 0:
#                 zeros+=1
#             temp = temp.next
#         temp2 = A
#         while temp2.next!=None:
#             if zeros>0:
#                 temp2.val=0
#                 zeros=zeros-1
#             else:
#                 temp2.val=1
#                 ones=ones-1
#             temp2=temp2.next
#         return A
#         # for i in range(zeros):
#         #     temp2.val = 0
#         #     temp2 = temp2.next
#         # for i in range(ones):
#         #     temp2.val = 0
#         #     temp2 = temp2.next
#         # # print(zeros,ones)
#         # return A
        

