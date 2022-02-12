def minimumPassesOfMatrix(matrix):
    passes = convertNegative(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < 0:
                return -1
    return passes-1


def convertNegative(matrix):
    queueOne = []
    queueTwo = []
    passes = 0
    # get all Positive val
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                queueOne.append([i, j])
    while queueOne:
        queueTwo = queueOne
        queueOne = []
        while queueTwo:
            row, col = queueTwo.pop(0)
            adjacent = getAdjacent(matrix, row, col)
            for i, j in adjacent:
                if matrix[i][j] < 0:
                    matrix[i][j] *= -1
                    queueOne.append([i, j])
        passes += 1
    return passes


def getAdjacent(matrix, i, j):
    ans = []
    if i > 0:
        ans.append([i-1, j])
    if i < len(matrix)-1:
        ans.append([i+1, j])
    if j > 0:
        ans.append([i, j-1])
    if j < len(matrix[0])-1:
        ans.append([i, j+1])
    return ans
