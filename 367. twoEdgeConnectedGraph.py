def twoEdgeConnectedGraph(edges):
    if len(edges) == 0:
        return True
    arrivalTime = [-1]*len(edges)
    start = 0
    if getMinArrivalTime(start, -1, 0, arrivalTime, edges):
        return False
    for time in arrivalTime:
        if time == -1:
            return False
    return True


def getMinArrivalTime(currentVertex, parent, currentTime, arrivalTime, edges):
    arrivalTime[currentVertex] = currentTime
    minArrivalTime = currentTime
    for destination in edges[currentVertex]:
        if arrivalTime[destination] == -1:
            minArrivalTime = min(minArrivalTime,
                                 getMinArrivalTime(destination, currentVertex, currentTime+1, arrivalTime, edges))
        elif destination != parent:  # check for circular node
            minArrivalTime = min(minArrivalTime, arrivalTime[destination])

    if minArrivalTime == currentTime and parent != -1:
        return -1
    return minArrivalTime
