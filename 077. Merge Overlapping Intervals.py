# Merge Overlapping Intervals
"""
Given a collection of intervals, merge all overlapping intervals.

For example:

Given [1,3],[2,6],[8,10],[15,18],

return [1,6],[8,10],[15,18].

Make sure the returned intervals are sorted.
"""

# intervals = [1,3],[2,6],[8,10],[15,18]
# intervals =  [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]
# intervals = list(intervals)
# a,b = intervals[0]
# out = []
# for c,d in intervals[1:]:
#     if max(a,c) > min(b,d): #do not overlap
#         out.append((c,d))
#     else:
#         while b > c:
#             break
#         out.append((a,d))
        
# print(out)
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, I):
        res = []
        I.sort(key=lambda i: i.start)
        for i in I:
            if not res or res[-1].end < i.start:
                res.append(i)
            else:
                res[-1].end = max(res[-1].end, i.end)
        return res 