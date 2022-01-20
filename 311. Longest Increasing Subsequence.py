def longestIncreasingSubsequence(array):
    seq = [None for x in array]
    lengths = [1 for x in array]
    maxLengthIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and lengths[j]+1 >= lengths[i]:
                lengths[i] = lengths[j+1]
                seq[i] = j
        if lengths[i] >= lengths[maxLengthIdx]:
            maxLengthIdx = i
    out = []
    while maxLengthIdx is not None:
        out.append(array[maxLengthIdx])
        maxLengthIdx = seq[maxLengthIdx]
    return list(reversed(out))
