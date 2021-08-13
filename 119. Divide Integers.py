# Divide Integers
"""
Divide two integers without using multiplication, division and mod operator.

Return the floor of the result of the division.

Example:

5 / 2 = 2
Also, consider if there can be overflow cases. For overflow case, return INT_MAX.

Note: INT_MAX = 2^31 - 1
"""
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        return 2**31-1 if A//B>(2**31-1) else A//B