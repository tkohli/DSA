from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = defaultdict()
        maxLen = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] not in dct:
                dct[s[right]] = 0
            dct[s[right]] += 1
            while dct[s[right]] > 1:
                dct[s[left]] -= 1
                left += 1
            right += 1

            maxLen = max(maxLen, right-left)
        return (maxLen)
