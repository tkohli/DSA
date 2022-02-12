def cycleInGraph(edges):
    n = len(edges)
    visited = [False for _ in range(n)]
    stack = [False for _ in range(n)]
    for node in range(n):
        if visited[node]:
            continue
        containsCycle = isNodeInCycle(node, edges, visited, stack)
    if containsCycle:
        return True
    return False


def isNodeInCycle(node, edges, visited, stack):
    visited[node] = True
    stack[node] = True
    neighbor = edges[node]
    for n in neighbor:
        if not visited[n]:
            isCycle = isNodeInCycle(n, edges, visited, stack)
            if isCycle:
                return True
        elif stack[n]:
            return True
    stack[node] = False
    return False
