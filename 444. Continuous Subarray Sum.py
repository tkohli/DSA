nums = [23,2,4,6,7]
k = 6

"""
we can do this in naive but optimization is great problem
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Check for multiples

nums =  23 2 4 6 7
k = 6
PrefixSum   reminder    Index
23          23%6 = 5    0
25          25%6 = 1    1
29          29%6 = 5    2

since we get same val i.e. the sub array between the previous 
remiander leads to our ans 
just to keep track of edge cases
"""

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0 :-1}
        total = 0

        for i,num in enumerate(nums):
            total+=num
            r = total%k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True
        return False