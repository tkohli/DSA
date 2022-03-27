"""
This is nice question and teaches me about CP 
this is very new way for me
"""


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        l = None  # prev val
        ans = 0
        for i in nums:
            if l is None:
                l = i
            elif l != i:
                l = None
                ans += 2
        return len(nums)-ans
