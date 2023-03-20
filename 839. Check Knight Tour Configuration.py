# Check Knight Tour Configuration
class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        dct = {}
        if grid[0][0]!=0:
            return False
        for i in range(len(grid)):
            for j in range(len(grid)):
                dct[grid[i][j]] = (i,j)

        n = 0
        while n<(len(grid)**2)-1:
            x,y = dct[n]
            if dct[n+1] in [(x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1),(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2)]:
                n+=1
            else:
                return False
        return True