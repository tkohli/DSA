class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            pass
            # return 0
        visited = [False for _ in range(len(isConnected))]
        count = 0
        for i in range(len(isConnected)):
            if visited[i] == False:
                count += 1
                visited[i] = True
                self.dfs(i, isConnected, visited)
        return (count)

    def dfs(self, i, isConnected, visited):
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and visited[j] == False:
                visited[j] = True
                self.dfs(j, isConnected, visited)
