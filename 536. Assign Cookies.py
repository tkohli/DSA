class Solution:
    # greedy
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        c = 0
        k = 0
        while k < len(s) and c < len(g):
            if s[k] >= g[c]:
                c += 1
            k += 1
        return c
