# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head :
            return None
        if not head.next:
            return TreeNode(head.val)
        prev = None
        s,f = head,head
        while f and f.next:
            prev = s
            f = f.next.next
            s = s.next
        if prev:
            prev.next = None
        root = TreeNode(s.val)
        head2 = s.next
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(head2)
        return root
        

        
        
        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        
        # def helper(l,r):
        #     if l>r:
        #         return None
        #     m = (l+r)//2
        #     node =TreeNode(arr[m])
        #     node.left = helper(l,m-1)
        #     node.right = helper(m+1,r)
        #     return node

        # return helper(0,len(arr)-1)

        