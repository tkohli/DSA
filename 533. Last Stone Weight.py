import heapq


class Solution:
    def lastStoneWeight(self, x: List[int]) -> int:
        h = [-elem for elem in stones]
        heapq.heapify(h)
        while len(h) > 1:
            a, b = heapq.heappop(h), heapq.heappop(h)
            heapq.heappush(h, -abs(a - b))
        return abs(h[0])
        # stones = []
        # for i in x:
        #     heappush(stones, -i)

        # while len(stones) > 1:
        #     x = heappop(stones)*-1
        #     y = heappop(stones)*-1

        #     if x == y:
        #         continue
        #     else:
        #         heappush(stones, abs(x-y)*-1)

        # return stones[-1]*-1 if len(stones)==1 else 0
