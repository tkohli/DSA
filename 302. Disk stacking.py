def diskStacking(disks):

    disks.sort(key=lambda disk: disk[2])
    heights = [h[2] for h in disks]
    Sequence = [None for _ in disks]
    maxHeight = 0
    for i in range(1, len(disks)):
        currentDisk = disks[i]
        for j in range(i):
            otherDisk = disks[j]
            if isValid(currentDisk, otherDisk):
                if heights[i] <= currentDisk[2]+heights[j]:
                    heights[i] = currentDisk[2]+heights[j]
                    Sequence[i] = j
        if heights[i] >= heights[maxHeight]:
            maxHeight = i

    seq = []
    while maxHeight is not None:
        seq.append(disks[maxHeight])
        maxHeight = Sequence[maxHeight]
    return (seq[::-1])


def isValid(c, o):
    return c[0] > o[0] and c[1] > o[1] and c[2] > o[2]
