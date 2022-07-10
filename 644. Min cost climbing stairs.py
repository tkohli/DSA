"""
						   __________
				      ___ | Final step
                 ___ | 20
            ___ | 15
_________ | 10

First step
we say that cost
cost = [10,15,20]
tmp =   10 15 30
r1 =    10  15
r2 =    10  15
"""
cost = [10, 15, 20]

cost.append(0)
dp = [cost[i] for i in range(len(cost))]
dp[0] = cost[0]
dp[1] = cost[1]
# keep track for 2 nodes only
for idx in range(2, len(dp)):
    dp[idx] += min(dp[idx-1], dp[idx-2])


# for i in range(len(cost)-3, -1, -1):
#             cost[i] += min(cost[i+1], cost[i+2])

#         return min(cost[0], cost[1])
# return dp[-1]
