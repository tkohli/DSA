"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1 = 0
        rob2 = 0
        for num in nums:
            temp = max(rob1+num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        # if len(nums)==0:
        #     return []
        # if len(nums)==1:
        #     return nums[0]
        # if len(nums)==2:
        #     return max(nums)
        # current = nums[1]
        # prev = nums[0]
        # for num in nums[2:]:
        #     if prev+num > current:
        #         current,prev = prev + num,current
        #     else:
        #         prev = current
        # return current
