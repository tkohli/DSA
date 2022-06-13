class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)]for j in range(n)]
        num = 1
        strRow, strCol = 0, 0
        endRow, endCol = n-1, n-1
        while strRow <= endRow and strCol <= endCol:
            for c in range(strCol, endCol+1):
                matrix[strRow][c] = num
                num += 1
            for r in range(strRow+1, endRow+1):
                matrix[r][endCol] = num
                num += 1
            for c in reversed(range(strCol, endCol)):
                if endRow == strRow:
                    break
                matrix[endRow][c] = num
                num += 1
            for r in reversed(range(strRow+1, endRow)):
                if endCol == strCol:
                    break
                matrix[r][strCol] = num
                num += 1
            strCol += 1
            strRow += 1
            endCol -= 1
            endRow -= 1
        return matrix
