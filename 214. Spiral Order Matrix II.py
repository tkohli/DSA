class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        current = 1 
        matrix = [[0 for x in range(A)] for x in range(A)]
        row,col,rowEnd,colEnd = 0,0,A-1,A-1
        while row<=rowEnd and col <= colEnd:
            for c in range(col,colEnd+1):
                matrix[row][c] = current
                current+=1
            for r in range(row+1,rowEnd+1):
                matrix[r][colEnd] = current
                current+=1
            for c in reversed(range(col,colEnd)):
                if row == rowEnd:
                    break
                matrix[rowEnd][c] = current
                current+=1
            for r in reversed(range(row+1,rowEnd)):
                if col==colEnd:
                    break
                matrix[r][col] = current
                current+=1
            row+=1
            col+=1
            colEnd-=1
            rowEnd-=1
        return matrix