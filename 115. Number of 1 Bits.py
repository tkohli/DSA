# Number of 1 Bits
"""
Problem Description

Write a function that takes an integer and returns the number of 1 bits it has.


Problem Constraints
1 <= A <= 109


Input Format
First and only argument contains integer A


Output Format
Return an integer as the answer


Example Input
Input1:
    11


Example Output
Output1:
3


Example Explanation
Explaination 1:
11 is represented as 1101 in binary
"""
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        # out = 0
        out = list(bin(A).replace("0b", ""))
        return out.count('1')