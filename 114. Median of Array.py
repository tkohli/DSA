# Median of Array
"""
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output

3
NOTE: IF the number of elements in the merged array is even, then the median is the average of n / 2 th and n/2 + 1th element. 

For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
"""
import math
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def get_max(self,A,p):
        if p==0:
            return -100000000
        else:
            return A[p-1]   
    def get_min(self,A,p):
        if p==len(A):
            return 1000000000
        else:
            return A[p]    

    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        lo=0
        hi=m
        combined=m+n
        while lo<=hi:
            partX=(lo+hi)/2
            partY=((combined+1)/2)-partX
            LeftX=self.get_max(A,partX)
            rightX=self.get_min(A,partX)
            LeftY=self.get_max(B,partY)
            rightY=self.get_min(B,partY)

            if LeftX<=rightY and LeftY<=rightX:
                if combined%2==0:
                    return (max(LeftX,LeftY)+min(rightX,rightY))/2.0
                else:
                    return max(LeftX,LeftY)
            if LeftX>rightY:
                hi=partX-1
            else:
                lo=partX+1
        return -1                    

# class Solution:
#     # @param A : tuple of integers
#     # @param B : tuple of integers
#     # @return a double
#     def findMedianSortedArrays(self, A, B):
#         C = list((list(A)+list(B)))
#         C.sort()
#         # print(C)
#         if len(C)%2 == 0:
#             return (C[len(C)//2]+C[(len(C)//2)+1])
#         else:
#             return float(C[len(C)//2])
