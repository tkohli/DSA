ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
"""
So this is a strait forward question find area of 2 rectangles and
see if they overlap then subtract area of overlapped rectangle 
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaOfA = (ax2-ax1)*(ay2-ay1)   # l*b
        areaOfB = (bx2-bx1)*(by2-by1)   # l*b
        areaOfOverlap = 0
        totalArea = 0
        # find overlap of X
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        xOverlap = right-left

        # find overlap of Y
        bottom = max(ay1, by1)
        top = min(ay2, by2)
        yOverlap = top-bottom

        if xOverlap > 0 and yOverlap > 0:
            areaOfOverlap = xOverlap*yOverlap

        return areaOfA+areaOfB-areaOfOverlap
