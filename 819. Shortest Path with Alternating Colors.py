# Shortest Path with Alternating Colors
class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        RED = 0
        BLUE = 1
        
        # build graph
        g0 = collections.defaultdict(list)
        g1 = collections.defaultdict(list)
        for u, v in red_edges:
            g0[u].append(v)
        for x, y in blue_edges:
            g1[x].append(y)
        g = [g0, g1]
        
        res = [float('inf')] * n
        
        def bfs(color):
            queue = [(0, color, 0)]
            visited = set()
            visited.add((0, color))
            while queue:
                node, color, step = queue.pop(0)
                res[node] = min(res[node], step)
                
                ncolor = 1 - color
                for nei in g[ncolor][node]:
                        if (nei, ncolor) not in visited:
                            queue.append((nei, ncolor, step +1))
                            visited.add((nei, ncolor))

        bfs(RED)   #start from 0 and  red edge first.
        bfs(BLUE)  #start from 0 and  blue edge first.
		
        return [x if x!=float('inf') else -1 for x in res]