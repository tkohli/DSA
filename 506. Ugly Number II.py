n = 10


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1] + [0]*(n-1)
        p2 = p3 = p5 = 0
        for i in range(1, n):
            ans[i] = min(ans[p2]*2, ans[p3]*3, ans[p5]*5)
            if ans[i] == ans[p2]*2:
                p2 += 1
            if ans[i] == ans[p3]*3:
                p3 += 1
            if ans[i] == ans[p5]*5:
                p5 += 1
        return ans[-1]
