import heapq


def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)

    minDistances = [float("inf") for _ in range(numberOfVertices)]
    minDistances[start] = 0

    visited = set()

    stack = [(start, 0)]
    while stack:
        vertex, currentMin = heapq.heappop(stack)
        visited.add(vertex)
        for edge in edges[vertex]:
            destination, cost = edge
            if destination in visited and currentMin+cost > minDistances[destination]:
                continue
            newPath = currentMin+cost
            currentCost = minDistances[destination]
            minDistances[destination] = min(newPath, currentCost)
            heapq.heappush(stack, ((destination, minDistances[destination],)))
    return list(map(lambda x: -1 if x == float("inf") else x, minDistances))
    # return minDistances
