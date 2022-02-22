from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for node, dest, cost in times:
            edges[node].append((dest, cost))

        visit = set()
        t = 0
        stack = [(0, k)]  # cost,node so we have min heap
        while stack:
            cost, dest,  = heapq.heappop(stack)
            if dest in visit:
                continue
            visit.add(dest)
            t = max(t, cost)

            for next, nextCost in edges[dest]:
                if next not in visit:
                    heapq.heappush(stack, ((t+nextCost), next))
                    # stack.append()
        if n != len(visit):
            return -1
        return t
