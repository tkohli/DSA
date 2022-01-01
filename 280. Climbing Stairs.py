class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        f1 = 1
        f2 = 1
        for i in range(n):
            temp = f1+f2
            f1 = f2
            f2 = temp
        return f1
