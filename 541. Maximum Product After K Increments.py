class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return (nums[0] + k) % MOD
        heapq.heapify(nums)
        while k > 0:
            t = heapq.heappop(nums)
            heapq.heappush(nums, t+1)
            k -= 1
        ans = 1
        print(nums)
        for i in nums:
            ans = (ans*i) % MOD
        return ans % MOD
