"""
-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Nearest gate and replace it with smallest val / dis from gate
if unreachable then don't change it's val
:)   Graph 
Optimization - let's start from gate then expand all sides BFS  
Can we do this simultaniously it will be faster and we need not to 
do work again and again
o/p = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
from collections import deque


rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
rows, cols = len(rooms), len(rooms[0])
visited = set()
q = deque()

for r in range(rows):
    for c in range(cols):
        if rooms[r][c] == 0:
            q.append([r,c])
            visited.add((r,c))

dis = 0
# now we can do a bfs 
while q:
    for i in range(len(q)):
        r,c = q.popleft()
        if rooms[r][c] == -1:
            continue
        # now go to all sides
        rooms[r][c] = dis

        if r>0 and (r-1,c)not in visited:
            q.append([r-1,c])
            visited.add((r-1,c))

        if r<rows-1 and (r+1,c) not in visited:
            q.append([r+1,c])
            visited.add((r+1,c))

        if c>0 and (r,c-1) not in visited:
            q.append([r,c-1])
            visited.add((r,c-1))


        if c<cols-1 and (r,c+1) not in visited:
            q.append([r,c+1])
            visited.add((r,c+1))


    dis+=1
        

for r in rooms:
    print(r)
