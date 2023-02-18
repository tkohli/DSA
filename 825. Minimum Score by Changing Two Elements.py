class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return min((nums[n-3]-nums[0]), min((nums[n-2]-nums[1]), nums[n-1]-nums[2]))
#         if len(nums)==3:
#             return 0
#         t = (sum(nums)//len(nums))
#         nums.sort()
#         nums[0] = t
#         nums[1] = t
        
#         return nums[-1]-nums[0]