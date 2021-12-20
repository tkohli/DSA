"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        target = 0
        i = 0
        out = []
        while i < len(nums)-2:
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] == target:
                    out.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[i]+nums[j]+nums[k] > target:
                    k -= 1
                else:
                    j += 1
            i += 1
        res = []
        [res.append(x) for x in out if x not in res]
        return res
