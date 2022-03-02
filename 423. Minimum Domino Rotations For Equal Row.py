tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
"""
Intuation is to check for first val in top 
and bottom and then check that is it valid or not 
"""
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for target in [tops[0],bottoms[0]]:
            missingTop = 0
            missingBottom = 0
            for idx in range(len(tops)):
                if tops[idx] != target and bottoms[idx]!=target:
                    break
                if tops[idx]!=target:
                    missingTop+=1
                if bottoms[idx]!=target:
                    missingBottom+=1
                if idx == len(tops)-1:
                    return min(missingTop,missingBottom)

        return -1