startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]
"""
Naive algo
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
print(jobs[0][2])
