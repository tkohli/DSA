nums = [1, 2, 3]
multipliers = [3, 2, 1]


# recursive and TLE :) Pain bro
class Solution:
    # time 2^n and M space
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Number of Operations
        m = len(multipliers)

        @lru_cache(None)
        def helper(left, right, op):
            if op == m:
                return 0

            return max(nums[left] * multipliers[op] + helper(left+1, right, op+1),
                       nums[right] * multipliers[op] + helper(left, right-1, op+1))

        return helper(0, len(nums)-1, 0)


# recursive with memomization and TLE :) Pain bro still
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Number of Operations
        m = len(multipliers)
        # for Right Pointer
        n = len(nums)
        memo = {}

        def dp(op, left):
            if op == m:
                return 0
            # If already computed, return
            if (op, left) in memo:
                return memo[(op, left)]
            l = nums[left] * multipliers[op] + dp(op+1, left+1)
            r = nums[(n-1)-(op-left)] * multipliers[op] + dp(op+1, left)
            memo[(op, left)] = max(l, r)
            return memo[(op, left)]
        # Zero operation done in the beginning
        return dp(0, 0)


class Solution:
    # m^2 time and space
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Number of Operations
        m = len(multipliers)
        # For Right Pointer
        n = len(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])
        return dp[0][0]


class Solution:
    # Time m^2
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [0] * (m + 1)
        for op in range(m - 1, -1, -1):
            next_row = dp.copy()
            # Present Row is now next_Row because we are moving upwards
            for left in range(op, -1, -1):
                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])
        return dp[0]
