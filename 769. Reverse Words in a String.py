# Reverse Words in a String

s = "the sky is blue"

class Solution:
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])
