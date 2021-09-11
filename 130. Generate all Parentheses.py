# Generate all Parentheses
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
"""
class Solution:
    # @param A : string
    # @return an integer
    def isValid(self, A):
        if A.count('(')==A.count(')') and  A.count('{')==A.count('}') and  A.count('[')==A.count(']'):
            return 1
        else:
            return 0