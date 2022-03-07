"""
This was a nice question almost solved it in the first trial 
let's try it again
"""
n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
from collections import defaultdict
# let's start by making a reverse adjacency matrix

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for start,to in edges:
            graph[to].append(start)

        memo = defaultdict(list)

        def dfs(src):
            if src in memo:
                return memo[src]
            for node in graph[src]:
                memo[src]+=[node]+dfs(node)

            memo[src] = list(set(memo[src]))
            return memo[src]

        for i in range(n):
            dfs(i)
        return (sorted(memo[i]) for i in range(n))