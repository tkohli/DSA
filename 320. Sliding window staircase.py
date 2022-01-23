def staircaseTraversal(height, maxSteps):
    currentNumberOfWays = 0
    waysToTop = [1]

    for currentheight in range(1, height+1):
        windowStart = currentheight-maxSteps+1
        windowEnd = currentheight+1
        if windowStart >= 0:
            currentNumberOfWays -= waysToTop[windowStart]
        currentNumberOfWays += waysToTop[windowEnd]
        waysToTop.append(currentNumberOfWays)

    return waysToTop[height]
