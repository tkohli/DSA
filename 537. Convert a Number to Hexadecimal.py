class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        map = "0123456789abcdef"
        res = ""
        if num < 0:
            num += 2**32
        while num > 0:
            dig = num % 16
            num = (num-dig)//16
            res += str(map[dig])
        return res[::-1]
