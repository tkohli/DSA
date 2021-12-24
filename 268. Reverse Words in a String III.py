class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s.split(" "))
        out = []
        for item in s:
            item = list(item)
            left, right = 0, len(item)-1
            while left < right:
                item[left], item[right] = item[right], item[left]
                left += 1
                right -= 1
            out.append("".join(item))
        return " ".join(out)
