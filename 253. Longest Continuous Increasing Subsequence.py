class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq = 1
        temp = 1
        for i in range(0, len(nums)-1):
            if nums[i] < nums[i+1]:
                temp += 1
            else:
                temp = 1
            seq = max(temp, seq)
        return seq
