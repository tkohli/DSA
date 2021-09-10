# Balanced Parantheses!
"""
Problem Description

Given a string A consisting only of '(' and ')'.

You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.



Problem Constraints
1 <= |A| <= 105



Input Format
First argument is an string A.



Output Format
Return 1 if parantheses in string are balanced else return 0.



Example Input
Input 1:

 A = "(()())"
Input 2:

 A = "(()"


Example Output
Output 1:

 1
Output 2:

 0


Example Explanation
Explanation 1:

 Given string is balanced so we return 1
Explanation 2:

 Given string is not balanced so we return 0
"""
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        balance = 0
        for b in A:
            if(b == '('):
                balance+=1
            else:
                balance-=1
            if(balance < 0):
                return 0
        
        if(balance):
            return 0
        return 1