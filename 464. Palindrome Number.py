class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        tmp = x
        while x > 0:
            num = num*10 + x % 10
            x //= 10
        return tmp == num
