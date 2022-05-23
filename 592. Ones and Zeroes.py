"""
Based on the first approach it seems like a counting problem 
But people are using 0/1 knapsack and it seems fair 
but there should be some other way around
"""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0, 0)}
        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros
            part_dp = set()
            for z, o, v in dp:
                if zeros + z <= m and ones + o <= n:
                    part_dp.add((zeros + z, ones + o, v + 1))
            for s in part_dp:
                dp.add(s)
        return max(v for _, _, v in dp)

        # dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
        # for strs in S:
        #     zeros = strs.count("0")
        #     ones = len(strs) - zeros
        #     for i in range(M, zeros - 1, -1):
        #         for j in range(N, ones - 1, -1):
        #             dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        # return dp[M][N]
