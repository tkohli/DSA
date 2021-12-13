class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        power = 1
        temp = 1
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                temp += 1
                # i+=1/
            else:
                temp = 1
            power = max(temp, power)
        return power
