# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    result = []
    while head is not None:
        result.append(head.value)
        head = head.next
    return result == result[::-1]
