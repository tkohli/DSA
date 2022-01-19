# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if slow != fast or fast is None or fast.next is None:
            return None

        # slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head
        # while head:
        #     head = head.next
        #     slow = slow.next
        #     if head == slow:
        #         return head
