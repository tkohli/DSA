def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    currentInterval = sortedIntervals[0]
    out = []
    out.append(currentInterval)
    for interval in sortedIntervals:
        currentStart, currentEnd = currentInterval
        nextStart, nextEnd = interval
        if currentEnd >= nextStart:
            currentInterval[1] = max(currentEnd, nextEnd)
        else:
            currentInterval = interval
            out.append(currentInterval)
    return (out)


# intervals = [1,3],[2,6],[8,10],[15,18]
print(mergeOverlappingIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
