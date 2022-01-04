# edge generation
def minimumAreaRectangle(points):
    cols = initCols(points)
    minArea = float("inf")
    edgesParallelToY = {}
    # start from right most
    sortedCols = sorted(cols.keys())
    for x in sortedCols:
        yValuesInCurrentCol = cols[x]
        yValuesInCurrentCol.sort()

        for currentIdx, y2 in enumerate(yValuesInCurrentCol):
            for prevIdx in range(currentIdx):
                y1 = yValuesInCurrentCol[prevIdx]
                pointString = str(y1)+":"+str(y2)
                if pointString in edgesParallelToY:
                    currentArea = (x-edgesParallelToY[pointString])*(y2-y1)
                    minArea = min(minArea, currentArea)
                edgesParallelToY[pointString] = x
    if minArea == float("inf"):
        return 0
    return minArea


def initCols(points):
    col = {}
    for point in points:
        x, y = point
        if x not in col:
            col[x] = []
        col[x].append(y)
    return col
