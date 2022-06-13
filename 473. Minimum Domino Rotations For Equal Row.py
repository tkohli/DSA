class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        for target in [tops[0], bottoms[0]]:
            missingBottom = missingTop = 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    break
                if tops[i] != target:
                    missingTop += 1
                if bottoms[i] != target:
                    missingBottom += 1
                if i == len(tops)-1:
                    return min(missingBottom, missingTop)
        return -1
