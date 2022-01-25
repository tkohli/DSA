def ambiguousMeasurements(measuringCups, low, high):
    memoization = {}
    return canMeasureInRange(measuringCups, low, high, memoization)


def canMeasureInRange(measuringCups, low, high, memoization):
    memoKey = hash(low, high)
    if memoKey in memoization:
        return memoization[memoKey]

    if low <= 0 and high <= 0:
        return False

    canMeasure = False
    for cup in measuringCups:
        cupLow, cupHigh = cup
        if low <= cupLow and cupHigh <= high:
            canMeasure = True
            break

        newLow = max(0, low-cupLow)
        newHigh = max(0, high-cupHigh)
        canMeasure = canMeasureInRange(
            measuringCups, newLow, newHigh, memoization)
        if canMeasure:
            break
    memoization[memoKey] = canMeasure
    return canMeasure


def hash(low, high):
    return str(low)+":"+str(high)
