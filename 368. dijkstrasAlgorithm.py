def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)

    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[0] = 0

    visited = set(0)

    while len(visited) != numberOfVertices:
        return minDistances


def getVertexWithMinDistance(distances, visited):
    currentMin = float('inf')
    vertex = -1
    for idx, distance in enumerate(distances):
        if idx in visited:
            continue
        if distance <= currentMin:
            vertex = idx
            currentMin = distance
    return vertex, currentMin
