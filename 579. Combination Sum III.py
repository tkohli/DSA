from itertools import combinations


class Solution:
    def combinationSum3(self, k, n):
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backTracking(comb, curSum, start):
            if len(comb) == k:
                if curSum == n:
                    res.append(comb[:])
                return

            for i in range(start, 10):
                backTracking(comb+[i], curSum+i, i+1)

        backTracking([], 0, 1)
        return res
