# Max Non Negative SubArray
"""
Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:  

If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.


Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109



Input Format
The first and the only argument of input contains an integer array A, of length N.



Output Format
Return an array of integers, that is a subarray of A that satisfies the given conditions.



Example Input
Input 1:

 A = [1, 2, 5, -7, 2, 3]
Input 2:

 A = [10, -1, 2, 3, -4, 100]


Example Output
Output 1:

 [1, 2, 5]
Output 2:

 [100]
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        sm = 0
        dct = {}
        dct[1] = []
        i = 1
        out = 1
        for a in A:
            if a >= 0:
                dct[i].append(a)
            else:
                i+=1
                dct[i] = []
        # print(dct)
        for item,value in dct.items():
            # print(item,value)
            if sum(value)> sm:
                sm = sum(value)
                out = item
            # sm = max(sum(value),sm)
            # out = item
        return (dct[out])
