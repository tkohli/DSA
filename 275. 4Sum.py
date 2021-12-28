nums = [-2, 2, -2, 2]
targetSum = 0
array = nums
allSum = {}
quadruplets = []    # output
for i in range(1, len(nums)-1):
    for j in range(i+1, len(nums)):
        # Going right and checking for that input
        currentSum = nums[i]+nums[j]
        difference = targetSum-currentSum
        if difference in allSum:
            for pair in allSum[difference]:
                quadruplets.append(pair+[nums[i], nums[j]])
    for k in range(0, i):
        currentSum = nums[i]+nums[k]
        if currentSum not in allSum:
            allSum[currentSum] = [[nums[i], nums[j]]]
        else:
            allSum[currentSum].append([nums[i], nums[j]])
print(quadruplets)
