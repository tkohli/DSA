# Count Unreachable Pairs of Nodes in an Undirected Graph
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            res = 1
            for n in graph[node]:
                res += dfs(n)
            return res
        
        components = []
        
        for i in range(n):
            temp = dfs(i)
            if temp != 0:
                components.append(temp)
        result = 0
        for i in components:
            result += (n - i) * i
        return result//2