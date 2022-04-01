class Solution:
    def intToRoman(self, num: int) -> str:
        sym = [
            ['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10],
            ['XL', 40], ['L', 50], ['XC', 90], ['C', 100],
            ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]
        ]
        ans = ""
        for symbol, val in sym[::-1]:
            count = num//val
            ans += (symbol*count)
            num -= (val*count)  # num = num % val
            if num == 0:    # early stopping
                return ans

        # res = ""
        # for s,val in reversed(sym):
        #     if num//val:
        #         count = num//val
        #         res += (s*count)
        #         num = num%val
        # return res
