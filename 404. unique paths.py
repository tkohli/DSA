m = 3
n = 7
matrix = [[1 for _ in range(n)] for __ in range(m)]
for i in range(1, m):
    for j in range(1, n):
        matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

print(matrix[-1][-1])
