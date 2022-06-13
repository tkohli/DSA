nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
"""
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
if we find 2 consecutive numbers same then goto right side 
while num is smaller the it's val and then swap it
while we find 0's change i else swap it with j and j+=1
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j


print(nums)
