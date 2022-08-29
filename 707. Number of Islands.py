class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()  # (i,j)

        def helper(i, j, grid):
            seen.add((i, j))
            stack = [(i, j)]
            while stack:  # len(stack)!=0
                tmp = []
                for idx in range(len(stack)):
                    m, n = stack.pop()
                    for r, c in [[m+1, n], [m-1, n], [m, n+1], [m, n-1]]:
                        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1" and (r, c) not in seen:
                            seen.add((r, c))
                            tmp.append((r, c))
                stack = tmp[:]
            return None
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in seen:
                    helper(i, j, grid)
                    count += 1
        return count
