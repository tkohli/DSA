class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Let create jobs array which zip startTime, endTime, profit together.
        Let sort our jobs in increasing order of startTime.
        Let dp[i] denote the maximum profit taking jobs in jobs[i...n-1] such that there is no overlapping time range.
        For the current jobs[i], we have 2 choice
        Don't pick ith job: dp(i+1)
        Pick ith job: We earn profit[i] and the next job must have the startTime >= arr[i].endTime to avoid time overlapping.
        So we have to find j from [i+1, n] so that arr[j].startTime >= arr[i].endTime
        Then we have choice dp(j) + profit[i].
        Choose the choice which leads maximum profits between 2 above choices.
        Finally, dp(0) is our result.
        """

        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)

        dp = {}

        def helper(i):
            if i == n:
                return 0
            if i in dp:
                return dp[i]

            ans = helper(i+1)  # choosing next
            # find non overlapping interval
            for j in range(i+1, n+1):
                if j == n or jobs[j][0] >= jobs[i][1]:
                    ans = max(ans, helper(j)+jobs[i][2])
                    break
            dp[i] = ans
            return ans

        return helper(0)
