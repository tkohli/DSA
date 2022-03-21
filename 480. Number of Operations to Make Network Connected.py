"""
1. Convert it to adjacency matrix
2. Find all number of components
3. Find all redundant edges

"""
n = 4
connections = [[0, 1], [0, 2], [1, 2]]


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1

        visited = set()
        queue = []
        count = 0
        matrix = [[] for _ in range(n)]
        for start, end in connections:
            matrix[end].append(start)
            matrix[start].append(end)

        def dfs(root):
            visited.add(root)
            for j in matrix[root]:
                if j not in visited:
                    dfs(j)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count-1


for i in range(n):
    if i not in visited:
        count += 1
        dfs(i)
print(count)
