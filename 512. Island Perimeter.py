class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def check(i, j, ans, N, M):
            if i == 0:
                ans += 1
            elif i > 0 and grid[i-1][j] == 0:
                ans += 1
            if i == N:
                ans += 1
            elif i < N and grid[i+1][j] == 0:
                ans += 1
            if j == 0:
                ans += 1
            elif j > 0 and grid[i][j-1] == 0:
                ans += 1
            if j == M:
                ans += 1
            elif j < M and grid[i][j+1] == 0:
                ans += 1
            return ans

        N = len(grid)-1
        M = len(grid[0])-1
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans = check(i, j, ans, N, M)
        return ans
