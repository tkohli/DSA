def maxSubsetSumNoAdjacent(array):
    if len(array)==0:
        return 0
    if len(array) == 1:
        return array[0]
    maxSum = [array[0],max(array[1],array[0])]
    for currentNum in array[2:]:
         maxSum.append(max(maxSum[-1],maxSum[-2]+currentNum))
    return maxSum[-1]

maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])
