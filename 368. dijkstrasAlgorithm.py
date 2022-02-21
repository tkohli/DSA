def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)

    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    visited = set(start)

    while len(visited) != numberOfVertices:
        vertex, currentMin = getVertexWithMinDistance(minDistances, visited)
        if currentMin == float("inf"):
            break
        visited.add(vertex)
        for edge in edges:
            destination, cost = edge
            if destination in visited:
                continue
            newPath = currentMin+cost
            currentCost = minDistances[destination]
            minDistances[destination] = min(newPath, currentCost)
    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))
    # return minDistances


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
