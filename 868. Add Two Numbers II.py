# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Approach1: reverse l1,l2 then add them and reverse the ans linkedlist :)
        Approach2: Use python and convert it to int add then make LL from it :)
        Approach3: The general approach is to iterate through the linked lists simultaneously, performing digit-wise addition and handling carries. Normalize the result and reverse the linked list if necessary.
        """

        # Helper function to calculate the size of a linked list
        def get_size(node):
            size = 0
            while node:
                node = node.next
                size += 1
            return size

        size1 = get_size(l1)
        size2 = get_size(l2)
        result_head = None
        current_node = None

        while l1 or l2:
            val1 = val2 = 0
            if size1 >= size2:
                val1 = 0 if not l1 else l1.val
                l1 = l1.next if l1 else None
                size1 -= 1

            if size2 >= size1 + 1:
                val2 = 0 if not l2 else l2.val
                l2 = l2.next if l2 else None
                size2 -= 1
            # print(val1+val2)
            new_node = ListNode(val1 + val2)
            new_node.next = result_head
            result_head = new_node

        carry = 0
        current_node = result_head

        while current_node:
            current_node.val += carry
            if current_node.val >= 10:
                current_node.val = current_node.val % 10
                carry = 1
            else:
                carry = 0

            if current_node.next is None and carry == 1:
                current_node.next = ListNode(1)
                break

            current_node = current_node.next

        # Reverse the resulting linked list
        prev = None
        current = result_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        result_head = prev

        return result_head
