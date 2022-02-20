class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 1
        currentEnd = intervals[0][1]
        for interval in intervals:
            start, end = interval
            if end > currentEnd:
                count += 1
                currentEnd = end
        return count
