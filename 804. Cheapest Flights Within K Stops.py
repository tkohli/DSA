class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # single souce shortest path
        dist = [float("inf")] * n
        dct = defaultdict(list)
        for f, t, p in flights:
            dct[f].append([t, p])
        queue = [(src, 0)]
        stops = 0
        while queue and stops <= k:
            tmp = []
            for node, cur in queue:
                for child, cost in dct[node]:
                    if cur+cost < dist[child]:
                        dist[child] = cur+cost
                        # we need total cost of reaching that element hence we are using dist[child]
                        tmp.append((child, dist[child]))
            queue = tmp[:]
            stops += 1
        print(dct)
        return dist[dst] if dist[dst] != float("inf") else -1
