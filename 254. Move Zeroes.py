class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        countZeros = 0
        i = 0
        while i < len(nums)-1:
            if nums[i] == 0:
                countZeros += 1
                nums.pop(i)
            else:
                i += 1
        nums += [0]*countZeros
