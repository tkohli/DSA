def maximizeExpression(array):
    if len(array) < 4:
        return 0
    maxOfA = [array[0]]
    maxOfAminusB = [float('-inf')]
    maxOfAminusBplusC = [float('-inf')]*2
    maxOfAminusBplusCminusD = [float('-inf')]*3

    for idx in range(1, len(array)):
        currentMax = max(maxOfA[idx-1], array[idx])
        maxOfA.append(currentMax)

    for idx in range(1, len(array)):
        currentMax = max(maxOfAminusB[-1], maxOfA[idx-1]-array[idx])
        maxOfAminusB.append(currentMax)

    for idx in range(2, len(array)):
        currentMax = max(
            maxOfAminusBplusC[-1], array[idx]+maxOfAminusB[idx-1])
        maxOfAminusBplusC.append(currentMax)

    for idx in range(3, len(array)):
        currentMax = max(maxOfAminusBplusCminusD[-1],
                         maxOfAminusBplusC[idx-1]-array[idx])
        maxOfAminusBplusCminusD.append(currentMax)

    return maxOfAminusBplusCminusD[-1]


print(maximizeExpression([3, 6, 1, -3, 2, 7]))
