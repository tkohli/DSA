# Domino and Tromino Tiling
"""
We are giving n and we have to find all possible ways by which we can
arrange domino and tromino to completely fill the 2 x n size matrix
link for image ref https://assets.leetcode.com/users/images/9a096afe-85f9-4358-a179-5563f960fc37_1639115832.0220907.png
                   https://assets.leetcode.com/users/images/6cbfc1b2-edda-402b-a386-27b29ce215cf_1639115869.433002.png
We get 2 different cases where we have previous gap and one where we do not have gaps
we have -

No Previous Gaps:

Place T1 and move to i+1: solve(i+1, previousGap=false)
Place T2 in pair and move to i+2: solve(i+2, previousGap=false)
Place either T3 or T4 (consider both cases) and move to i+2 with gap at i+1th column: 2*solve(i+2, previousGap=true)
Previous Gaps Present:

Place T5 or T6 & fill previous gap (consider only 1 bcoz depending on current configuration, only 1 grid out of them will fit) and move to i+1 with no previous gaps remaining: solve(i+1, previousGap=false)
Place T2 & fill previous gap and move to i+1 with gap present in ith column: solve(i+1, previousGap=true)

That's it! We now just recursively fill the grid using above cases. If we reach the end of the grid (column i = n) 
with no previous gaps, then we know that we found 1 possible way of tiling grid, so we return 1. Otherwise if we 
exceed bounds of grid or reach end with previous gaps remaining, then we return false.

"""


class Solution:
    def numTilings(self, n: int) -> int:
        dp = [[0, 0] for _ in range(3)]
        dp[1], dp[2] = [1, 1], [2, 2]
        for i in range(3, n+1):
            dp[i % 3][0] = dp[(i-1) % 3][0] + dp[(i-2) %
                                                 3][0] + 2*dp[(i-2) % 3][1]
            dp[i % 3][1] = dp[(i-1) % 3][0] + dp[(i-1) % 3][1]
        return dp[n % 3][0] % 1_000_000_007

        # Time Complexity : O(N) same space
        # dp = [[0, 0] for _ in range(n+2)]
        # dp[1], dp[2] = [1, 1], [2, 2]
        # for i in range(3, n+1):
        #     dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2*dp[i-2][1]
        #     dp[i][1] = dp[i-1][0] + dp[i-1][1]
        # return dp[n][0] % 1000000007

        # Time Complexity : O(3^N)
        # def solve(i, previous_gap):
        #     if i > n: return 0
        #     if i == n: return not previous_gap
        #     if previous_gap:
        #         return solve(i+1, False) + solve(i+1, True)
        #     return solve(i+1, False) + solve(i+2, False) + 2*solve(i+2, True)
        # return solve(0, False) % 1000000007
