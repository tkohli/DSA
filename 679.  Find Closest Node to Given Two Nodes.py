"""
We are givin 2 nodes and graph we need to find the closest element from both
we first start with BFS and keep track of all elements with their distance
then find common node then return node with lowest value
"""


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def BFS(root):
            distance = defaultdict(lambda: float("inf"))
            queue = deque([root])
            level = 0
            while queue:
                node = queue.popleft()
                if distance[node] <= level:
                    continue
                distance[node] = level
                for neighbor in graph[node]:
                    queue.append(neighbor)
                level += 1
            return distance

        n = len(edges)
        graph = [[] for _ in range(n)]

        for node, to in enumerate(edges):
            if to != -1:
                graph[node].append(to)

        a = BFS(node1)
        b = BFS(node2)
        options = []  # common

        for i in range(n):
            if a[i] != float("inf") and b[i] != float("inf"):
                options.append((max(a[i], b[i]), i))

        if not options:
            return -1

        return min(options)[1]
