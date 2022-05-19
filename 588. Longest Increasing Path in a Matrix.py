"""
This is very similar to max increasing path sum
We will go to an element and the store the max value 
that we can get by taking it to min i.e. find all bigger 
values and then sum it so we don't have to do sum at each index 
[9, 9, 4]
[6, 6, 8]
[2, 1, 1]

dp =
[-1, -1, -1]
[-1, -1, -1]
[-1, -1, -1]

dp =>
[[1, 1, 2]
 [2, 2, 1]
 [3, 4, 2]]
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1 for i in range(cols)] for j in range(rows)]

        def dfs(r, c):
            if dp[r][c] >= 0:
                return dp[r][c]  # we have already found the max path len

            maxPathLen = 0
            for nextRow, nextCol in [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]:
                # if (nextRow >= 0 and nextRow > rows) and (nextCol >= 0 and nextCol > cols) and matrix[nextRow][nextCol] > matrix[r][c]:
                # incresing
                if 0 <= nextRow < rows and 0 <= nextCol < cols and matrix[nextRow][nextCol] > matrix[r][c]:
                    maxPathLen = max(maxPathLen, dfs(nextRow, nextCol))

            dp[r][c] = maxPathLen+1
            return dp[r][c]

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))

        return ans
