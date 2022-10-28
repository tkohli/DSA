nums = [1, 3, 5, 2]
cost = [2, 3, 1, 14]
order = sorted(range(len(nums)), key=nums.__getitem__)
nums = [nums[i] for i in order]
cost = [cost[i] for i in order]

front = [0] * len(nums)
curr = 0
for i in range(len(nums) - 1):
    curr += cost[i]
    front[i + 1] = front[i] + curr * (nums[i + 1] - nums[i])

sol = front[len(nums) - 1]
curr, back = cost[-1], 0
for i in reversed(range(len(nums) - 1)):
    back += curr * (nums[i + 1] - nums[i])
    sol = min(sol, front[i] + back)
    curr += cost[i]
print(sol)
