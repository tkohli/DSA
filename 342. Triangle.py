class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = triangle[-1][:]
        for w in reversed(triangle[:-1]):
            for idx, ele in enumerate(w):
                ans[idx] = min(ans[idx], ans[idx+1])+ele
        return ans[0]
