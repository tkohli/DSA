"""
nums = [1,5,11,5]
o/p True as 11 == 1+5+5
we take target = sum(nums)/2
We can do recusrion or we can use DP 
we make a set in which will store all possible sum of subarray in
our set  
"""
nums = [1,5,11,5]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2==1:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for t in dp:
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp = nextDP

        if target in dp:
            return True
        return False