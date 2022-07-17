# K Inverse Pairs Array
"""
if we are given [1..n] array then when we 1 in first position it has 0 inversions
if we put 2 in first position then we have 1 inversion 
similarly if we have n in first position that means we have n-1 inversions
5 x x x x creates 4 new inverse pairs
x 5 x x x creates 3 new inverse pairs
...
x x x x 5 creates 0 new inverse pairs
thus dp[n+1][k] = sum_{x=0..n} dp[n][k-x]
"""

n = 4
k = 5
mod = 10**9 + 7
dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    dp_new = []
    s = 0
    for j in range(k + 1):
        s += dp[j]
        if j >= i + 1:
            s -= dp[j - i - 1]
        s %= mod
        dp_new.append(s)
    dp = dp_new
print(dp)
