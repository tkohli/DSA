nums = [2, 3, 4, 6]
ans = 0
freq = {}
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        key = nums[i] * nums[j]
        ans += freq.get(key, 0)
        freq[key] = 1 + freq.get(key, 0)
print(8*ans)
