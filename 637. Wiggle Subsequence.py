nums = [1, 7, 4, 9, 2, 5]
"""
there exists DP solution but mainly it is about finding alternatives min and max
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prevDiff = nums[1]-nums[0]
        if prevDiff != 0:
            count = 2
        else:
            count = 1
        for i in range(2, len(nums)):
            diff = nums[i]-nums[i-1]
            if (diff > 0 and prevDiff <= 0) or (diff < 0 and prevDiff >= 0):
                count += 1
                prevDiff = diff
        return count
