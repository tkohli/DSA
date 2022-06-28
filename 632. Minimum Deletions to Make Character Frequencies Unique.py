from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        freq = []
        for k,v in c.items():
            freq.append(v)
        freq.sort(reverse=True)
        delCount = 0
        maxFreq = len(s)
        for f in freq:
            if f > maxFreq:
                delCount+= (f-maxFreq)
                f = maxFreq
            maxFreq = max(0,f-1)
        return delCount