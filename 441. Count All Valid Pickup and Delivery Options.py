"""
We have i dilivery and we have to find all possible seq
all valid pickup/delivery possible sequence such that
delivery(i) is always after of pickup(i). 
If we want to deliver i items that means 
currently there are i undelivered items
then there are also unpicked different choices 
we can say

if unpicked > 0
    we have choice to pick from one of those orders

if undelivered > unpicked
    we ahave the choice to deliver any one of them 


Tabulation (Bottom-Up DP)
or some clever math that is tough to come up with
"""
class Solution:
    def countOrders(self, n: int) -> int:
        dp = [[0]*(n+1) for i in range(n+1)]
        mod = 1000000007
        for unpicked in range(n+1):
            for undelivered in range(unpicked,n+1):
                if not unpicked and not undelivered:
                    dp[unpicked][undelivered] = 1

                if unpicked>0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked-1][undelivered]
                    dp[unpicked][undelivered]%=mod
                if undelivered>unpicked:
                    dp[unpicked][undelivered] +=(
                        undelivered-unpicked
                    ) * dp[unpicked][undelivered-1]
                    dp[unpicked][undelivered]%=mod
        return dp[n][n]