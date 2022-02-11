from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        lenS1 = len(s1)
        lenS2 = len(s2)
        if lenS2 < lenS1:
            return False
        c = Counter(s1)
        for i in range(lenS2-lenS1+1):
            if Counter(s2[i:i+lenS1]) == c:
                return True
        return False
