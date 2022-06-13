"""
We are given size of envelopes and and we have find the max num 
that we can put inside each other 
So we sort increasing in first dimension and decreasing on second
After that make a dp and check for which envelope can be inserted where

keeping the track of longest increasing sequence
[[5, 4], [6, 4], [6, 7], [2, 3]]
[[4,5],[4,6],[6,7],[2,3],[1,1]]
"""
from bisect import bisect_left


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for l, b in envelopes:
            idx = bisect_left(dp, b)
            if idx == len(dp):
                dp.append(b)
            else:
                dp[idx] = b
        return len(dp)
