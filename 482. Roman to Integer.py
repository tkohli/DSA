class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        ans = 0
        for i, ch in enumerate(s):
            if i < len(s)-1 and dct[ch] < dct[s[i+1]]:
                ans -= dct[ch]
            else:
                ans += dct[ch]
        return ans
