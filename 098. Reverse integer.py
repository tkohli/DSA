# Reverse integer
"""
Problem Description

You are given an integer N and the task is to reverse the digits of the given integer. Return 0 if the result overflows and does not fit in a 32 bit signed integer


Look at the example for clarification.



Problem Constraints
N belongs to the Integer limits.



Input Format
Input an Integer.



Output Format
Return a single integer denoting the reverse of the given integer.



Example Input
Input 1:

 x = 123


Input 2:

 x = -123


Example Output
Output 1:

 321


Output 2:

 -321


Example Explanation
 If the given integer is negative like -123 the output is also negative -321.
"""
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        neg = 0
        if A < 0:
            neg = 1
        A = abs(A)
        
        A = list(str(A))
        A.reverse()
        a = "".join(map(str,A))
        if int(a) > 2147483647:
            return 0
        if neg == 1:
            return -(int(a))
        return int(a)