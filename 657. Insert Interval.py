intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
"""
Question similar to merge interval
will use stack more importantly we use 2 array left and right
all value smaller on left 
bigger on right and merged values in middle
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        return left+[newInterval]+right
