class Solution:
    def findNeighbor(self,i,j,image,curCol):
            array = []
            if i>0:
                if image[i-1][j] == curCol:
                    array.append((i-1,j))
            if i<len(image)-1:
                if image[i+1][j] == curCol:
                    array.append((i+1,j))
            if j>0:
                if image[i][j-1] == curCol:
                    array.append((i,j-1))
            if j<len(image[0])-1:
                if image[i][j+1] == curCol:
                    array.append((i,j+1))
            return array
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if(image[sr][sc]==newColor):
            return image
        
        curCol = image[sr][sc]
        queue = [(sr,sc)]
        while queue:
            # change color then find neighbor
            for block in range(len(queue)):
                i,j = queue.pop()
                if image[i][j]!=curCol:
                    continue
                image[i][j] = newColor
                tmp = self.findNeighbor(i,j,image,curCol)
                for t in tmp:
                    queue.append(t)
        return image