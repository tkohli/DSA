class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0

        col = set()
        diagonal = set()
        antiDiagonal = set()
        output = []
        result = []

        def backtracking(r):
            nonlocal n, col, diagonal, antiDiagonal, output, result

            if r == n:
                result.append(output[:])
                return

            for c in range(n):
                if c in col or (r+c) in diagonal or (r-c) in antiDiagonal:
                    continue
                col.add(c)
                diagonal.add(c+r)
                antiDiagonal.add(r-c)
                output.append("."*c+'Q'+'.'*(n-c-1))
                backtracking(r+1)
                col.remove(c)
                diagonal.remove(c+r)
                antiDiagonal.remove(r-c)


class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return []

        col = set()
        diagonal = set()    # determined by r+c
        antidiagonal = set()
        # output = []
        result = 0

        def backtrack(r):
            nonlocal n, col, diagonal, antidiagonal, result
            if r == n:
                result += 1
                return

            for c in range(n):
                if c in col or (r+c) in diagonal or (r-c) in antidiagonal:
                    continue

                col.add(c)
                diagonal.add(r+c)
                antidiagonal.add(r-c)
                backtrack(r+1)
                col.remove(c)
                diagonal.remove(r+c)
                antidiagonal.remove(r-c)

        backtrack(0)
        return (result)
