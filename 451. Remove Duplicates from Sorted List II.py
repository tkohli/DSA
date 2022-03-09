# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None:
        #     return None
        # if head.next is None:
        #     return head

        newHead = ListNode(0,head)
        
        tmp = newHead
        
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head = head.next
                tmp.next  = head.next
            else:
                tmp = tmp.next
                
            head = head.next
        
        return newHead.next