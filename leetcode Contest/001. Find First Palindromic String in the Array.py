"""
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
"""


class Solution(object):
    def firstPalindrome(self, words):
        """
        this could be implemented in 2 pointer method also 
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if word[::-1] == word:
                return word
        return ""
