"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                self.swap(nums, mid, low)
                mid += 1
                low += 1
            elif nums[mid] == 2:
                self.swap(nums, mid, high)
                high -= 1
            else:
                mid += 1

    def swap(nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
