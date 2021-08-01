# Grid Unique Paths
"""
A robot is located at the top-left corner of an A x B grid (marked ‘Start’ in the diagram below).

Path Sum: Example 1

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
              OR  : (0, 0) -> (1, 0) -> (1, 1)

"""
from math import factorial
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        return factorial(A+B-2)//factorial(A-1)//factorial(B-1)

# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @return an integer
#     def uniquePaths(self, A, B):
#         def factorial(N):
#             out = 1
#             for n in range(2,N+1):
#                 out*=1
#             return out
#         return factorial(A+B-2)//factorial(A-1)//factorial(B-1)
#         # return min(m+n-2, n - 1)