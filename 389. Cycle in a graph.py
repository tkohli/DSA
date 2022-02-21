def cycleInGraph(edges):
    numberOfNodes = len(edges)
    visited = [False for i in range(numberOfNodes)]
    currentlyInStack = [False for i in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if visited[node]:
            continue
        # check for cycle
	if containsCycle(node, edges, visited, currentlyInStack):
		return True
    return False


def containsCycle(node, edge, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True

    neighbor = edge[node]
    for neigh in neighbor:
        if not visited[neigh]:
            # do BFS
            containsSubCycle = containsCycle(
                neigh, edge, visited, currentlyInStack)
            if containsSubCycle:
                return True
        elif currentlyInStack[neigh]:
            return True
    currentlyInStack[node] = False
    return False
