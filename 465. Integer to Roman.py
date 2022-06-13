"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

but just simply add val for 4, 9, 40, 90,400,900 etc then simple
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        sym = [
            ['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10],
            ['XL', 40], ['L', 50], ['XC', 90], ['C', 100],
            ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]
        ]
        res = ""
        for s, val in reversed(sym):
            if num//val:
                count = num//val
                res += (s*count)
                num = num % val
        return res
