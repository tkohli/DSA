class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        h = dict()

        for a in A:
            for b in B:
                p = -(a+b)
                if p in h:
                    h[p] += 1
                else:
                    h[p] = 1
        count = 0

        for c in C:
            for d in D:
                p = c+d
                if p in h:
                    count += h[p]

        return count
