class Solution:
    def isHappy(self, n):
        if n == 1:
            return True
        seen = set()
        while n not in seen:
            seen.add(n)
            n = list(str(n))
            sq = [int(i)**2 for i in n]
            n = sum(sq)
            if n == 1:
                return True

        return n == 1
