cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] # append(0)
     # [1, 100, 2, 3, 3, 103, 4, 5, 104, 6, 6]

"""
We need a dp way to keep track of min val 
similar to house robber but I have to dry run the code
Note : append extra 0 to out dp or cost array top start with 
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [cost[i] for i in range(len(cost))]
        dp[0]=cost[0]
        dp[1]=cost[1]
        # keep track for 2 nodes only
        for idx in range(2,len(dp)):
            dp[idx] = min(dp[idx-1],dp[idx-2])+cost[idx]

        return dp[-1]