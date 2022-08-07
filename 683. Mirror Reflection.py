"""
There is a special square room with mirrors on each of the four walls. 
Except for the southwest corner, there are receptors on each of the 
remaining corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest 
corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that 
the ray meets first.

"""


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        firstly divide the p and q with 2 while they are even 
        we are making it into a unit square with side = 2 
        If p = odd, q = even: return 0
        If p = even, q = odd: return 2
        If p = odd, q = odd: return 1
        """
        while p % 2 == 0 and q % 2 == 0:
            p, q = p // 2, q // 2
        return 1 - p % 2 + q % 2

        if p == q:
            return 1
        while p % 2 == 0 and q % 2 == 0:
            p = p//2
            q = q//2
        if p % 2 != 0:
            if q % 2 != 0:
                return 1
            return 0
        else:
            return 2
