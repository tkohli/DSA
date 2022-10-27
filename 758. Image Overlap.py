from typing import List

from numpy import left_shift

"""
First impression this is a tough question 
would try a naive solution then see for any valid optimization 

Therefore, a simple idea is that one could come up all possible 
overlapping zones, by shifting the image matrix, and then simply 
count within each overlapping zone.
"""


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        N = len(img1)

        def shiftAndCount(xShift, yShift, move, ref):  # Helper function
            """
            here move is matrix that we are moving
            ref is matrix we take as reference 
            moving one matrix up is equivalent to
            moving the other matrix down
            """
            leftShiftCount, rightShiftCount = 0, 0
            for rRow, mRow in enumerate(range(yShift, N)):
                for rCol, mCol in enumerate(range(xShift, N)):
                    if move[mRow][mCol] == 1 and move[mRow][mCol] == ref[rRow][rCol]:
                        leftShiftCount += 1
                    if move[mRow][rCol] == 1 and move[mRow][rCol] == ref[rRow][mCol]:
                        rightShiftCount += 1
            return max(leftShiftCount, rightShiftCount)

        maxOverLaps = 0
        for i in range(N):
            for j in range(N):
                maxOverLaps = max(maxOverLaps, shiftAndCount(j, i, img1, img2))
                maxOverLaps = max(maxOverLaps, shiftAndCount(j, i, img2, img1))
        return maxOverLaps
