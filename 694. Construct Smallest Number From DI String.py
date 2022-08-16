class Solution:
    def smallestNumber(self, s: str) -> str:
        res, lasti = [], 0
        for i, c in enumerate(s + 'I', 1):
            if c == 'I':
                res += range(i, lasti, -1)
                lasti = i
        return ''.join(map(str, res))
