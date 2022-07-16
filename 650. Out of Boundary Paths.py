m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        @lru_cache(None)
        def moves(move, row, col):
            if row == m or row < 0 or col < 0 or col == n:
                return 1
            if move == 0:
                return 0
            move -= 1

            return (moves(move, row+1, col)+moves(move, row, col+1)+moves(move, row-1, col)+moves(move, row, col-1)) % ((10**9)+7)

        return moves(maxMove, startRow, startColumn)


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        # define the dp array
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]

        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

                # if the dp array at this position contains some value(not -1) then it means it has been computed earlier
                # so we don't need to compute again, hence return whatever value is present in dp.
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]

                # otherwise compute the value
            a = solve(i-1, j, maxMove - 1)
            b = solve(i+1, j, maxMove - 1)
            c = solve(i, j-1, maxMove - 1)
            d = solve(i, j+1, maxMove - 1)

        # store the computed value in dp array so that we do not need to compute it again when the same input occurs again.
            dp[i][j][maxMove] = a + b + c + d
            return dp[i][j][maxMove]

        return solve(startRow, startColumn, maxMove) % 1000000007
