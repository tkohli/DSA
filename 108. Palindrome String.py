# Palindrome String
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        l = [c.lower() for c in A if c.isalnum()]
        return 1 if l == l[::-1] else 0