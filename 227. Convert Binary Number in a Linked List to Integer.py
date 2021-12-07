# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        
        num = head.val
        while head.next:
            num = (num<<1)| head.next.val
            head=head.next
        return num
        
        
        # binaryNum = []
        # num=head
        # while num is not None:
        #     binaryNum.append(num.val)
        #     num = num.next
        # Number = 0
        # for idx,num in enumerate(binaryNum[::-1]):
        #     Number+=(num*(2**idx))
        # return Number
            
            