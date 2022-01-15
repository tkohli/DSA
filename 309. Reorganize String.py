from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)
        freq = sorted(freq.items(), key=lambda k: -k[1])
        if freq[0][1] >= n / 2 + 1:
            return ""
        res = [""] * n
        i = 0
        for x, fx in freq:  # iterate the sorted dictionary
            for _ in range(fx):  # loop fx times
                if i >= n:
                    i = 1  # go back to index 1
                res[i] = x
                i += 2
        return "".join(res)
