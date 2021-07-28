#Pick from both sides!
"""
Problem Description

Given an integer array A of size N.

You can pick B elements from either left or right end of the array A to get maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.


Problem Constraints
1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the maximum possible sum of elements you picked.



Example Input
Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:

 A = [1, 2]
 B = 1


Example Output
Output 1:

 8
Output 2:

 2
"""

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def fastest_solve(self, A, B):
        """
        Time complexity = O(n) | Space complexity = O(1)
        Run time outputs: 267 ms	15644 KB
        We first take sum of last B digits then we find 
        local maximas by changing the numbers such that 
        every time maximum number is returned 
        """
        temp = sum(A[len(A)-B:])
        max_sum = temp
        for i in range(B):
            temp = (temp - A[i-B]) + A[i]
            if temp > max_sum:
                max_sum = temp
        return (max_sum)


    def other_solve(self, A, B):
        """
        Time complexity = O(n) | Space complexity = O(1)
        Run time outputs: 349 ms	16132 KB
        """
        left = A[:B]
        val = sum(left)
        imax = val
        for i in range(B):
            rem = left.pop()
            add = A.pop()
            val = (val-rem) + add
            imax = max(imax, val)
        return (imax)
