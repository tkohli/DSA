# def longestIncreasingSubsequence(array):
#     seq = [None for x in array]
#     lengths = [1 for x in array]
#     maxLengthIdx = 0
#     for i in range(len(array)):
#         currentNum = array[i]
#         for j in range(0, i):
#             otherNum = array[j]
#             if otherNum < currentNum and lengths[j]+1 >= lengths[i]:
#                 lengths[i] = lengths[j+1]
#                 seq[i] = j
#         if lengths[i] >= lengths[maxLengthIdx]:
#             maxLengthIdx = i
#     out = []
#     while maxLengthIdx is not None:
#         out.append(array[maxLengthIdx])
#         maxLengthIdx = seq[maxLengthIdx]
#     return list(reversed(out))

def longestIncreasingSubsequence(array):
    seq = [None for x in array]
    indices = [None for x in range(len(array)+1)]
    length = 0
    for i, num in enumerate(array):
        newLength = binarySearch(1, length, indices, array, num)
        seq[i] = indices[newLength-1]
        indices[newLength] = i
        length = max(length, newLength)
    maxLengthIdx = indices[length]
    out = []
    while maxLengthIdx is not None:
        out.append(array[maxLengthIdx])
        maxLengthIdx = seq[maxLengthIdx]
    return list(reversed(out))


def binarySearch(startIdx, endIdx, indices, array, num):
    if startIdx > endIdx:
        return startIdx
    middleIdx = (startIdx+endIdx)//2
    if array[indices[middleIdx]] < num:
        startIdx = middleIdx+1
    else:
        endIdx = middleIdx-1
    return binarySearch(startIdx, endIdx, indices, array, num)
