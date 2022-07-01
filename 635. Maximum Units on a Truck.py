from cProfile import label


boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
"""
boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]
Since we have fixed truckSize and we need max boxes so we do sorting
"""
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]
        cost = 0
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        for numBox,numUnit in boxTypes:
            boxes = min(numBox,truckSize)
            truckSize-=boxes
            cost += (boxes*numUnit)
            if truckSize==0:
                return cost
        return cost            