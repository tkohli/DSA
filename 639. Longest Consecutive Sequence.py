nums = [100, 4, 200, 1, 3, 2]
"""
We can sort it then use sliding window 
but if we are not allowed to sort the data then 
change it to a set and then find a valid starting point it could be a 
next lower value i.e. if we were given 1,2,3,4,5 and we start from 1 
then we check that any value lower than one is not available in nums 
so we avoid duplicate checking
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxlen = 0
        for num in nums:
            if num-1 not in nums:
                tmp = 0
                while num in nums:
                    tmp += 1
                    num += 1
                maxlen = max(tmp, maxlen)
        return maxlen
