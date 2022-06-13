class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        k = k % (len(grid) * len(grid[0]))

        linear = []
        for level in grid:
            linear.extend(level)
        linear = linear[-k:] + linear[:-k]

        l = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = linear[l]
                l += 1
        return grid
