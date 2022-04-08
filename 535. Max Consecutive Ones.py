class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window = 0
        i = 0
        while i < len(nums):
            tmp = i
            while tmp < len(nums) and nums[tmp] == 1:
                tmp += 1
            window = max(window, tmp-i)
            i = tmp+1
        return window
