class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        k = nums[len(nums)//2]
        ans = 0
        for num in nums:
            ans+=abs(num-k)
        return ans
        