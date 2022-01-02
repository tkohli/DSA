class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        res = 0
        for song in time:
            if song % 60 == 0:
                res += d[0]
            else:
                res += d[60 - song % 60]

            d[song % 60] += 1
        return res
