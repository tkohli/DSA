# Search in Bitonic Array
"""
Problem Description

Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.

NOTE:

A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.


Problem Constraints
3 <= N <= 105

1 <= A[i], B <= 108

Given array always contain a bitonic point.

Array A always contain distinct elements.



Input Format
First argument is an integer array A denoting the bitonic sequence.

Second argument is an integer B.



Output Format
Return a single integer denoting the position (0 index based) of the element B in the array A if B doesn't exist in A return -1.



Example Input
Input 1:

 A = [3, 9, 10, 20, 17, 5, 1]
 B = 20
Input 2:

 A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
 B = 30


Example Output
Output 1:

 3
Output 2:

 -1


Example Explanation
Explanation 1:

 B = 20 present in A at index 3
Explanation 2:

 B = 30 is not present in A
"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # if B in A:
        #     return A.index(B)
        # else:
        #     return -1
        n = len(A)
        if n==0:
            return -1
        elif n==1:
            return 0 if A[0]==B else -1

        l,r = 0, n-1

        def find_b(l, r):
            if l>r:
                return -1

            mid = l + (r-l)//2

            if mid == 0 or mid==n-1:
                return -1

            if A[mid]> A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] > A[mid+1]:
                return find_b(l, mid-1)
            else:
                return find_b(mid+1, r)
        
        def b_s(l,r):
            if l>r:
                return -1
            
            mid = l + (r-l)//2

            if A[mid]==B:
                return mid
            elif A[mid] > B:
                return b_s(l, mid-1)
            else:
                return b_s(mid+1, r)
        
                
        def rb_s(l,r):
            if l>r:
                return -1
            
            mid = l + (r-l)//2

            if A[mid]==B:
                return mid
            elif A[mid] < B:
                return rb_s(l, mid-1)
            else:
                return rb_s(mid+1, r)
        
        p = find_b(0, n-1)
        if p==-1:
            return b_s(0, n-1)
        else:
            bs = b_s(0, p)
            if bs!=-1:
                return bs

            return rb_s(p+1, n-1)