# Reverse String
"""
Given a string S, reverse the string using stack.

Example :

Input : "abc"
Return "cba"
"""
class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        lst = list(A)
        lstrev = [a for a in lst[::-1]]
        return "".join(lstrev)
