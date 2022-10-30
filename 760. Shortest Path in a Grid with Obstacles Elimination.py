from collections import deque
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # basic idea is to a bfs so we reach the last pos within best time
        # and somehow maintain number of obstacles less than or equal to k

        rows, cols = len(grid), len(grid[0])
        target = (rows-1, cols-1)  # this will be easy toc check

        # the shortest path will be Manhattan distance i.e.
        # diagonal passing in rectangle following down and right steps
        if k >= rows + cols - 3:
            return rows + cols - 2

        # to optimize we make a tuple with row,col,k
        # where k is remaining quota to eliminate obstacles
        state = (0, 0, k)  # starting point

        # queue to store steps and state
        queue = deque([(0, state)])
        seen = set([state])
        while queue:
            steps, (row, col, k) = queue.popleft()

            # we reach the target here
            if (row, col) == target:
                return steps

            # explore the four directions in the next step
            for new_row, new_col in [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]:
                # if (new_row, new_col) is within the grid boundaries
                if (0 <= new_row < rows) and (0 <= new_col < cols):
                    new_eliminations = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations)
                    # add the next move in the queue if it qualifies
                    if new_eliminations >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps + 1, new_state))

        # did not reach the target
        return -1
