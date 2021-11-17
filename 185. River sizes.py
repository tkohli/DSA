def riverSizes(matrix):
    sizes = [] 
    visited = [[False for i in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited [i][j]:
                continue
            # if not visited then traverse the matrix and 
            traverseNode(i,j,matrix,visited,sizes)
    return sizes

def traverseNode(i,j,matrix,visited,sizes):
    currentRiverSize = 0
    # now use DFS iteratively 
    nodesToExplore = [[i,j]] # stack
    while  len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i,j,matrix,visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i,j,matrix,visited):
    unvisitedNeighbor = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbor.append([i - 1,j])
    if i < len(matrix)-1 and not visited[i + 1][j]:
        unvisitedNeighbor.append([i + 1,j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbor.append([i,j - 1])
    if j < len(matrix[0])-1 and not visited[i][j+1]:
        unvisitedNeighbor.append([i,j+1])
    return unvisitedNeighbor
