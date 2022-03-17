"""
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

we can optimize this further by using first row and col to use it as in-place
hashing which will give us constant space
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [1]*len(matrix)
        col = [1]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        for r in range(len(row)):
            if row[r] == 0:
                for i in range(len(matrix[0])):
                    matrix[r][i] = 0
        for j in range(len(col)):
            if col[j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
