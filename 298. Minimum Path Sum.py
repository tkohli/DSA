class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid[0] = [sum(grid[0][:i]) for i in range(1, len(grid[0])+1)]
        for i in range(1, len(grid)):
            grid[i][0] = grid[i-1][0]+grid[i][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = min(grid[i-1][j]+grid[i][j],
                                 grid[i][j-1]+grid[i][j])

        return grid[-1][-1]
