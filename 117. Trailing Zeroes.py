# Trailing Zeroes
"""
Problem Description

Given an integer A, count and return the number of trailing zeroes.



Problem Constraints
1 <= A <= 109



Input Format
First and only argument is an integer A.



Output Format
Return an integer denoting the count of trailing zeroes.



Example Input
Input 1:

 A = 18
Input 2:

 A = 8


Example Output
Output 1:

 1
Output 2:

 3


Example Explanation
Explanation 1:

 18 in binary is represented as: 10010, there is 1 trailing zero.
Explanation 2:

 8 in binary is represented as: 1000, there are 3 trailing zeroes.
"""
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        out = list(bin(A).replace("0b", ""))
        count = 0
        for a in out[::-1]:
            if a == '0':
                count+=1
            if a == '1':
                break
            
        return count
