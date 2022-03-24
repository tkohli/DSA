"""
There are only 2 island make a bridge to connect
we can only go 4 directions so that makes easy for us to implement it
grid = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]


So first we start by doing a dfs and find out an island
then we mark all of those visited and then we do BFS such
that everytime we extend our radius we increase the val of our bridge.

Seems simple - it is just gonna be lengthy very
"""
from collections import deque


grid = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
    1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        # helper array to do dfs/bfs in 4 directions
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def invalid(r, c):
            return r < 0 or c < 0 or r == N or c == N

        def dfs(r, c):
            if (invalid(r, c) or not grid[r][c] or (r, c) in visit):
                return
            visit.add((r, c))
            for dr, dc in directions:
                dfs(dr+r, dc+c)

        def bfs():
            res = 0
            q = deque(visit)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()       # if we were using list then just pop(0)
                    for dr, dc in directions:
                        if invalid(r+dr, dc+c) or (r+dr, dc+c) in visit:
                            continue
                        else:
                            if grid[r+dr][c+dc]:
                                return res
                            q.append([r+dr, dc+c])
                            visit.add((r+dr, dc+c))
                res += 1

        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:     # first side of island
                    dfs(i, j)
                    return bfs()
