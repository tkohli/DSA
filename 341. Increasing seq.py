array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
length = [1 for a in array]
seq = [None for a in array]
maxLengthIdx = 0
for i in range(len(array)):
    currentNum = array[i]
    for j in reversed(range(i)):
        otherNum = array[j]
        if currentNum > otherNum and length[i] <= length[j]+1:
            length[i] = length[j]+1
            maxLengthIdx = max(i, maxLengthIdx)
            seq[i] = j
print(length)
out = []
while maxLengthIdx is not None:
    out.append(array[maxLengthIdx])
    maxLengthIdx = seq[maxLengthIdx]
print(list(reversed(out)))
