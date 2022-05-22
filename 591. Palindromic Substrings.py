class Solution:
    def countSubstrings(self, s: str) -> int:
        # naive solution
        ans = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                t = s[i:j]
                if t == t[::-1]:
                    ans += 1
        return ans


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def expandFromPoint(i, j):
            cnt = 0
            while i >= 0 and j < n and s[i] == s[j]:
                cnt += 1
                i -= 1
                j += 1
            return cnt

        ans = 0
        for i in range(len(s)):
            ans += expandFromPoint(i, i)
            ans += expandFromPoint(i, i+1)

        return ans
