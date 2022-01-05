class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ar = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ar.append(1)
            else:
                ar[-1] += 1
        count = 0
        for i in range(1, len(ar)):
            count += min(ar[i-1], ar[i])
        return count
