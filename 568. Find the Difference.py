class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)
        ans = ""
        for ch in t:
            if ch not in s or s[ch] != t[ch]:
                ans += ch

        return ans
