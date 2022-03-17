class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        tmp = 1
        while tmp <= n:
            if tmp == n:
                return True
            tmp *= 3
        return False
