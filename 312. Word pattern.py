class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dct = {}
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        for char, val in zip(pattern, s):
            # print(i, j)
            # if char==val:
            #     return False
            if char not in dct:
                if val in dct.values():
                    return False
                dct[char] = val
            if dct[char] != val:
                return False

        return True
