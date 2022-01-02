def waterfallStreams(array, source):
    rowAbove = array[0][:]  # copy
    rowAbove[source] = -1  # water coming
    # Now moving down or splitting
    for row in range(1, len(array)):
        currentRow = array[row][:]
        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]
            hasWater = valueAbove < 0
            hasBlock = currentRow[idx] == 1
            if not hasWater:
                continue
            if not hasBlock:
                currentRow[idx] += valueAbove
                continue
            splitWater = valueAbove/2
            # Right
            rightIdx = idx
            while rightIdx+1 < len(rowAbove):
                rightIdx += 1
                if rowAbove[rightIdx] == 1:
                    break
                if currentRow[rightIdx] != 1:
                    currentRow[rightIdx] += splitWater
                    break
            leftIdx = idx
            while leftIdx-1 >= 0:
                leftIdx -= 1
                if rowAbove[leftIdx] == 1:
                    break
                if currentRow[leftIdx] != 1:
                    currentRow[leftIdx] += splitWater
                    break
        rowAbove = currentRow
    return list(map(lambda x: x*-100, rowAbove))
