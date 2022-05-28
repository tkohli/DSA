class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # ans = len(nums)
        # for i in range(len(nums)):
        #     ans+=(i-nums[i])
        # return ans

        n = len(nums)
        return ((n * (n+1)) // 2) - sum(nums)
