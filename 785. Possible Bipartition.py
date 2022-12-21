class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(n + 1)]
        for n1, n2 in dislikes:
            g[n1].append(n2)
            g[n2].append(n1)
        color = [0] * (len(g))  # => [0, 1, -1, -1, 1]
        for i in range(1, len(g)):
            if color[i]:
                continue
            queue = [i]
            color[i] = 1
            while queue:
                node = queue.pop()
                for adj in g[node]:
                    if color[node] == color[adj]:
                        # print(False)
                        return False
                    elif color[adj] == 0:
                        queue.append(adj)
                        color[adj] = -color[node]
        return True
