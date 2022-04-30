from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        We can see that we are given values of a/b so we make a weighted graph 
        representing a->b with w and b->a with 1/w
        """
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1/val

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1

            if y in graph[x]:
                return graph[x][y]

            # if we cannot find it directly then search for other way around

            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    tmp = dfs(i, y, visited)
                    if tmp == -1:
                        continue
                    else:
                        return graph[x][i] * tmp

            return -1

        res = []
        for q in queries:
            res.append(dfs(q[0], q[1], set()))
        return res
