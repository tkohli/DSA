def sameBsts(arrayOne, arrayTwo):
    if len(arrayTwo) == 0 and len(arrayTwo) == 0:
        return True
    if arrayOne[0] != arrayTwo[0] or len(arrayOne) != len(arrayTwo):
        return False

    smallerOne = getSmaller(arrayOne)
    smallerTwo = getSmaller(arrayTwo)
    bigOne = getBigOrEqual(arrayOne)
    bigTwo = getBigOrEqual(arrayTwo)
    return sameBsts(smallerOne, smallerTwo) and sameBsts(bigOne, bigTwo)


def getSmaller(array):
    nums = []
    for a in array[1:]:
        if a < array[0]:
            nums.append(a)
    return nums


def getBigOrEqual(array):
    nums = []
    for a in array[1:]:
        if a >= array[0]:
            nums.append(a)
    return nums
