"""
Combination sum became coin change 2 :)
it is like all questions are now becoming coin change 2
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        @lru_cache(None)  # we can use Dp to memomize the array
        def helper(target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            ans = 0
            for num in nums:
                if num > target:
                    break
                ans += helper(target-num)
            return ans

        return helper(target)

        # dp = [0 for i in range(target+1)]
        # dp[0] = 1
        # for i in range(1,target+1):
        #     for num in nums:
        #         if num <= i:
        #             dp[i] += dp[i-num]
        # print(dp)
        # return dp[-1]
