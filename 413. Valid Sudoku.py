class Solution:
    """
    We can also make 3 set and keep track of val while traversing
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if not self.sudokuHelper(i, j, board):
                    return False
        return True

    def sudokuHelper(self, i, j, board):
        num = board[i][j]
        for x in range(9):
            if num == board[i][x]:
                if x == j:
                    continue
                return False
            if num == board[x][j]:
                if x == i:
                    continue
                return False
        m = (i // 3)*3
        n = (j // 3)*3
        for x in range(m, m+3):
            for y in range(n, n+3):
                if x == i and y == j:
                    continue
                if num == board[x][y]:
                    return False
        return True
