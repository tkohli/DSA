class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        M = 10**9 + 7
        self.count = 0

        @lru_cache(None)
        def dfs(pos, steps):
            if steps == 0 and pos == endPos:
                return 1
            if steps == 0:
                return 0
            return dfs(pos-1, steps-1) + dfs(pos+1, steps-1) % M

        ans = dfs(startPos, k)
        return ans % M
