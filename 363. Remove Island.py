def removeIslands(matrix):
    onesConnectedToBorder = [[False for i in matrix[0]] for j in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            rowIsBorder = i == 0 or i == len(matrix)-1
            colIsBorder = j == 0 or j == len(matrix[0])-1
            isBorder = (rowIsBorder or colIsBorder)
            if not isBorder:
                continue
            if matrix[i][j] != 1:
                continue
            expandFromBorder(matrix, i, j, onesConnectedToBorder)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and onesConnectedToBorder[i][j] == False:
                matrix[i][j] = 0

    return matrix


def expandFromBorder(matrix, r, c, onesConnectedToBorder):
    stack = [(r, c)]
    while stack:
        curRow, curCol = stack.pop()
        if onesConnectedToBorder[curRow][curCol]:
            continue
        onesConnectedToBorder[curRow][curCol] = True
        neighbors = getNeighbors(matrix, curRow, curCol)
        for neighbor in neighbors:
            r, c = neighbor
            if matrix[r][c] == 1:
                stack.append(neighbor)


def getNeighbors(matrix, i, j):
    arr = []
    row, col = len(matrix), len(matrix[0])
    if i-1 >= 0:
        arr.append((i-1, j))
    if i+1 < row:
        arr.append((i+1, j))
    if j-1 >= 0:
        arr.append((i, j-1))
    if j+1 < col:
        arr.append((i, j+1))
    return arr
