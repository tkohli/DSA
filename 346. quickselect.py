def quickselect(array, k):
    return quickSelectHelper(array, 0, len(array)-1, k-1)


def quickSelectHelper(array, start, end, position):
    while True:
        if start > end:
            raise Exception('Nope')
        pivotIdx = start
        leftIdx = start+1
        rightIdx = end
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        array[pivotIdx], array[rightIdx] = array[rightIdx], array[pivotIdx]
        if rightIdx == position:
            return array[rightIdx]
        if rightIdx > position:
            end = rightIdx-1
        else:
            start = rightIdx+1
