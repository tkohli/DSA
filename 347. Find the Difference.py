from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        for ch in t:
            if s[ch] < t[ch]:
                return ch
