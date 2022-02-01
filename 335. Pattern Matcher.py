def patternMatcher(pattern, string):
    if len(pattern) > len(string):
        return []
    newPattern = getNewPattern(pattern)
    didSwitch = newPattern[0] != pattern[0]
    counts = {'x': 0, 'y': 0}
    firstYPos = getCountsAndYPos(newPattern, counts)
    if counts['y']:
        for lenX in range(1, len(string)):
            lenY = (len(string)-(lenX*counts['x']))/counts['y']
            if lenY < 0 or lenY % 1 != 0:
                continue
            lenY = int(lenY)
            yIdx = firstYPos*lenX
            x = string[: lenX]
            y = string[yIdx: yIdx + lenY]
            potentialMatch = [x if s == 'x' else y for s in newPattern]
            # map(lambda char x: if char == 'x' else 'y', newPattern)
            if string == "".join(potentialMatch):
                return [x, y] if not didSwitch else [y, x]
    else:
        lenX = len(string)/counts['x']
        if lenX % 1 == 0:
            lenX = int(lenX)
            x = string[:lenX]
            potential = map(lambda char: x, newPattern)
            if string == "".join(potential):
                return [x, ""] if not didSwitch else ["", x]
    return []


def getNewPattern(pattern):
    pattern = list(pattern)
    if pattern[0] == 'x':
        return pattern
    else:
        pattern = ['x' if 'y' in p else 'y' for p in pattern]
        return (pattern)


def getCountsAndYPos(newPattern, counts):
    Ypos = None
    for i, ch in enumerate(newPattern):
        counts[ch] += 1
        if ch == 'y' and Ypos is None:
            Ypos = i
    return Ypos
