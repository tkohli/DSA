class Solution:
    def titleToNumber(self, S: str) -> int:
        ans = 0
        for s in S:
            ans *= 26
            i = ord(s)-64
            ans = ans+i
        return ans
