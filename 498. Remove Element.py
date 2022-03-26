"""
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, 
with the first two elements of nums being 2.
It does not matter what you leave beyond the 
returned k (hence they are underscores).
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        j = len(nums)-1
        i = 0
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                k += 1
                i += 1
        return k
