# Pair With Given Difference
"""
Problem Description

Given an one-dimensional unsorted array A containing N integers.

You are also given an integer B, find if there exists a pair of elements in the array whose difference is B.

Return 1 if any such pair exists else return 0.



Problem Constraints
1 <= N <= 105
-103 <= A[i] <= 103
-105 <= B <= 105


Input Format
First argument is an integer array A of size N.

Second argument is an integer B.



Output Format
Return 1 if any such pair exists else return 0.



Example Input
Input 1:

 A = [5, 10, 3, 2, 50, 80]
 B = 78
Input 2:

 A = [-10, 20]
 B = 30


Example Output
Output 1:

 1
Output 2:

 1


Example Explanation
Explanation 1:

 Pair (80, 2) gives a difference of 78.
Explanation 2:

 Pair (20, -10) gives a difference of 30 i.e 20 - (-10) => 20 + 10 => 30

"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A = sorted(A)
        for i in range(len(A)):
            for j in range(len(A)-1, i, -1):
                if abs(A[i] - A[j]) == abs(B):
                    return 1
                if A[i] - A[j] > B:
                    break
                
        return 0
