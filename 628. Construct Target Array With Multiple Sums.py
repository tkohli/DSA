class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        # make a max heap
        target = [-a for a in target]
        heapify(target)
        while True:
            x = -heappop(target)
            total -= x
            if x == 1 or total == 1:
                return True
            if x<total or total == 0 or x%total == 0:
                return False
            x%=total
            total += x
            heappush(target,-x)
            