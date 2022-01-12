# for efficient algo avoid repeated steps(summing)
def maximumSumSubmatrix(matrix, size):
    sums = createSumMatrix(matrix)
    maxSumSubMatrix = float("-inf")

    for row in range(size-1, len(matrix)):
        for col in range(size-1, len(matrix[row])):
            total = sums[row][col]

            touchesTopBorder = row-size < 0
            if not touchesTopBorder:
                total -= sums[row-size][col]

            touchesleftBorder = col-size < 0
            if not touchesleftBorder:
                total -= sums[row][col-size]

            leftorRight = touchesleftBorder or touchesTopBorder
            if not leftorRight:
                total += sums[row-size][col-size]

            maxSumSubMatrix = max(maxSumSubMatrix, total)

    return maxSumSubMatrix


def createSumMatrix(matrix):
    sums = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]
    # for first row
    for idx in range(1, len(matrix[0])):
        sums[0][idx] = sums[0][idx-1] + matrix[0][idx]
    # for first col
    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx-1][0] + matrix[idx][0]

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            sums[row][col] = sums[row][col-1] + sums[row-1][col] + \
                matrix[row][col] - sums[row-1][col-1]
    print(sums)
    return sums
