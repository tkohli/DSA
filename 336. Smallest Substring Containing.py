def smallestSubstringContaining(bigString, smallString):
    targetCharCount = getCharCount(smallString)
    subStringBounds = getSubStringBounds(bigString, targetCharCount)
    start, end = subStringBounds
    if end == float("inf"):
        return ""
    return bigString[start:end+1]


def getSubStringBounds(string, targetCharCount):
    subStringBounds = [0, float("inf")]
    subStringCharCount = {}
    numUniqueCharCounts = len(targetCharCount.keys())
    numuniqueCharFound = 0
    left = 0
    right = 0
    while right < len(string):
        rightChar = string[right]
        if rightChar not in targetCharCount:
            right += 1
            continue
        increaseCharCount(rightChar, subStringCharCount)
        if subStringCharCount[rightChar] == targetCharCount[rightChar]:
            numuniqueCharFound += 1
            while numuniqueCharFound == numUniqueCharCounts and left <= right:
                subStringBounds = getclosureBounds(
                    left, right, subStringBounds[0], subStringBounds[1])
                leftChar = string[left]
                if leftChar not in targetCharCount:
                    left += 1
                    continue
                if subStringCharCount[leftChar] == targetCharCount[leftChar]:
                    numuniqueCharFound -= 1
                decreaseCharCount(leftChar, subStringCharCount)
                left += 1
        right += 1
    return subStringBounds


def getclosureBounds(idx1, idx2, idx3, idx4):
    return [idx1, idx2] if idx2-idx1 < idx4-idx3 else [idx3, idx4]


def getCharCount(string):
    counts = {}
    for ch in string:
        increaseCharCount(ch, counts)
    return counts


def increaseCharCount(ch, counts):
    if ch not in counts:
        counts[ch] = 1
    else:
        counts[ch] += 1


def decreaseCharCount(ch, counts):
    counts[ch] -= 1
