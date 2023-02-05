from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        p = Counter(p)
        ans = []
        for i in range(n-m+1):
            if i == 0:
                window = Counter(s[:m])
            else:
                window[s[i-1]] -= 1
                window[s[i+m-1]] += 1
                # if window[s[i-1]] <= 0:
                #     window.pop(s[i-1])
            if window == p:
                ans.append(i)
        return ans