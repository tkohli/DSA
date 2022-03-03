grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

"""
We go border traversal and the change all border to 2
then traverse the map find all connected segments
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def expand(i,j):
            queue = [[i,j]]
            while queue:
                row,col = queue.pop()
                grid[row][col] = '2'
                arr = getCoordinates(row,col)
                for row,col in arr:
                    if grid[row][col]=='1':
                        queue.append([row,col])

        def getCoordinates(i,j):
            arr = []
            if i>0:
                arr.append([i-1,j])
            if i<len(grid)-1:
                arr.append([i+1,j])
            if j>0:
                arr.append([i,j-1])
            if j<len(grid[0])-1:
                arr.append([i,j+1])
            return arr
        queue = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    expand(i,j)
                    count+=1
        return (count)