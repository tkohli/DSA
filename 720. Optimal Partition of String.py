class Solution:
    def partitionString(self, s: str) -> int:
        i = j = 0
        cnt = 0
        while j < len(s):
            tmp = ""
            while i < len(s) and s[i] not in tmp:
                tmp += (s[i])
                i += 1
            else:
                cnt += 1
                j = i
        return cnt
