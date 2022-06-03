# this i9s nave solution but TLE
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                ans += self.matrix[i][j]
                # print(self.matrix[i][j],i,j)
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


class NumMatrix(object):
    def __init__(self, matrix):
        if matrix is None or not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sums = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.sums[i][j] = matrix[i-1][j-1] + self.sums[i][j -
                                                                  1] + self.sums[i-1][j] - self.sums[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sums[row2+1][col2+1] - self.sums[row2+1][col1] - self.sums[row1][col2+1] + self.sums[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


"""
[3, 0, 1, 4, 2], 
[5, 6, 3, 2, 1], 
[1, 2, 0, 1, 5], 
[4, 1, 0, 1, 7], 
[1, 0, 3, 0, 5]]



[[3, 3, 4, 8, 10], 
[8, 14, 18, 24, 27], 
[9, 17, 21, 28, 36],
[13, 22, 26, 34, 49], 
[14, 23, 30, 38, 58]]

"""
