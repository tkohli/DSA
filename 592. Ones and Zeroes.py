"""
Based on the first approach it seems like a counting problem 
But people are using 0/1 knapsack and it seems fair 
but there should be some other way around
"""

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
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
print(dp)
