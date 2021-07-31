# Next Similar Number
"""
Problem Description

Given a number A in a form of string.

You have to find the smallest number that has same set of digits as A and is greater than A.

If A is the greatest possible number with its set of digits, then return -1.



Problem Constraints
 1 <= A <= 10100000

 A doesn't contain leading zeroes.



Input Format
First and only argument is an numeric string denoting the number A.



Output Format
Return a string denoting the smallest number greater than A with same set of digits , if A is the largest possible then return -1.



Example Input
Input 1:

 A = "218765"
Input 2:

 A = "4321"


Example Output
Output 1:

 "251678"
Output 2:

 "-1"


Example Explanation
Explanation 1:

 The smallest number greater then 218765 with same set of digits is 251678.
Explanation 2:

 The given number is the largest possible number with given set of digits so we will return -1.

"""
class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        number = list(str(A))
        for i in range(n-1,0,-1): 
            if number[i] > number[i-1]: 
                x = number[i-1] 
                smallest = i 
                for j in range(i+1,n): 
                    if number[j] > x and number[j] < number[smallest]: 
                        smallest = j 

                number[smallest],number[i-1] = number[i-1], number[smallest] 
                number[i:] = sorted(number[i:]) 
                return "".join(number)
        
        return -1