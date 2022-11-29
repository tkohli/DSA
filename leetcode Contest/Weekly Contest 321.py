# Find the Pivot Integer
class Solution:
    def pivotInteger(self, n: int) -> int:
        total = 0
        for i in range(n+1):
            total += i
        print(total)
        x = 0
        for i in range(1, n+1):
            x += i

            if x == total:
                return (i)
            total -= i
        return -1


# Append Characters to String to Make Subsequence
s = "coaching"
t = "coding"


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return (len(t)-j)


# Remove Nodes From Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(inf, head)
        stack = [dummyHead]

        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack[-1].next = head
            stack.append(head)
            head = head.next

        return dummyHead.next
