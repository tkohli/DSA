class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        water = 0
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    queue.append((i,j))
                else:
                    water+=1
        if water == 0:
            return -1

        ans = 0
        while queue and water:
            tmp = []
            for m,n in queue:
                for x,y in [(m-1,n),(m,n-1),(m+1,n),(m,n+1)]:
                    if 0<=x<r and 0<=y<c and grid[x][y] == 0:
                        grid[x][y] = 1
                        tmp.append((x,y))
                        water -=1
            ans+=1
            queue = tmp[:]
            
        return ans if water ==0 else -1


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        water = 0
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    queue.append((i,j))
                else:
                    water+=1
        if water == 0:
            return -1

        def dfs(queue):
            nonlocal water
            tmp = []
            ans = 0
            for m,n in queue:
                for i,j in [(m-1,n),(m,n-1),(m+1,n),(m,n+1)]:
                    if 0<=i<r and 0<=j<c and water and grid[i][j] == 0:
                        grid[i][j] = 1
                        water-=1
                        tmp.append((i,j))
            if tmp==[]:
                return 0
            return 1+dfs(tmp)

        ans = dfs(queue)
        return ans if water ==0 else -1
