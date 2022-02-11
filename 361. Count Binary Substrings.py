class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, cur = 0, 1
        out = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                out += min(prev, cur)
                prev = cur
                cur = 1
            else:
                cur += 1
        return min(prev, cur)+out
