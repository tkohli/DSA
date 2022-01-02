from collections import Counter


class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt = Counter(s)
        num = 0
        for word in s:
            if word == 'a':
                num += 1
            if cnt['b'] == 0:
                return True
            elif word == 'b' and num == cnt['a']:
                return True
            elif word == 'b' and num != cnt['a']:
                return False
        return True
