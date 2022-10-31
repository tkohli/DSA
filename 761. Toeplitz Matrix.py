matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # O(m*n) TIme O(1) space

        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

        # x,y = 0,0
        # for col in range(len(matrix[0])):
        #     x = 0
        #     y = col
        #     tmp = matrix[x][y]
        #     while x < len(matrix) and y < len(matrix[0]):
        #         if matrix[x][y]!=tmp:
        #             return False
        #         x += 1
        #         y += 1

        # for row in range(len(matrix)):
        #     y = 0
        #     x = row
        #     tmp = matrix[x][y]
        #     while x < len(matrix) and y < len(matrix[0]):
        #         if matrix[x][y]!=tmp:
        #             return False
        #         x += 1
        #         y += 1
        # return True

        #         Faster run time but not efficient
        # O(m*n) TIme O(n) space
        # dp = matrix[0]
        # for row in matrix[1:]:
        #     dp.pop()
        #     dp.insert(0, row[0])
        #     if dp != row:
        #         return False
        # return True

        # O(m*n) TIme O(n) space
        # groups = {}
        # for r, row in enumerate(matrix):
        #     for c, val in enumerate(row):
        #         if r-c not in groups:
        #             groups[r-c] = val
        #         elif groups[r-c] != val:
        #             return False
        # return True
