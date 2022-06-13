class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ""
        while columnNumber:
            columnNumber -= 1
            ans = s[columnNumber % 26]+ans
            columnNumber //= 26
        return ans
