s = "acfgbd"
k = 2

dp = [0]*26
for ch in s:
    i = ord(ch)-ord("a")
    # dp[s[i + 1]] = 1 + max(dp[reachable]),
    # where abs(s[i + 1] - reachable) <= k
    dp[i] = 1 + max(dp[max(0, i-k):min(26, i+k+1)])
print(max(dp))
