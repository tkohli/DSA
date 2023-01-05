class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        arrow = 1
        prevStart, prevEnd = points[0]
        for currStart, currEnd in points[1:]:
            if currStart > prevEnd:
                arrow += 1
                prevEnd = currEnd
        return arrow
