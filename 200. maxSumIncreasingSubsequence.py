def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    maxSumIdx = 0
    sums = array[:]
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(i):
            otherNum = array[j]
            if otherNum<currentNum and sums[j]+currentNum>sums[i]: # Strictly increasing
                sums[i] = sums[j]+currentNum
                sequences[i] = j
        if sums[i]>sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array,sequences,maxSumIdx) ]

def buildSequence(array,sequences,maxSumIdx):


print(maxSumIncreasingSubsequence([1,2,3,4,5]))