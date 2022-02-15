def mergeSortedArrays(arrays):
    sortedArray = []
    arrayElementIdx = [0 for a in arrays]
    while True:
        smallest = []
        for idx in range(len(arrays)):  # k times loop
            currentArray = arrays[idx]
            elementIdx = arrayElementIdx[idx]
            if elementIdx == len(currentArray):
                continue
            smallest.append(
                {'arrayIdx': idx, 'nums': currentArray[elementIdx]})
        if len(smallest) == 0:
            break
        nextItem = getMinValue(smallest)
        sortedArray.append(nextItem['nums'])
        arrayElementIdx[nextItem['arrayIdx']] += 1
    return sortedArray


def getMinValue(items):
    minValueIdx = 0
    for i in range(1, len(items)):
        if items[minValueIdx]['nums'] >= items[i]['nums']:
            minValueIdx = i
    return items[minValueIdx]
