# Word Break
s = "leetcode"
wordDict = ["leet","code"]
"""

As we can se that we do not have a great way of finding out 
all sub strings of our s string and then checking if that substring is 
available in our dict so we try to find out this in countinous way

for every ch find if its sub string word is in our dct
we start with this dp 0- False 1 - True
   l e e t c o d e
[1,0,0,0,0,0,0,0,0]

At index 3 we find leet in dct so update
   l e e t c o d e
[1,0,0,0,1,0,0,0,0]

At index 7 we find code in dct so update
   l e e t c o d e
[1,0,0,0,1,0,0,0,1]
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True

        return dp[-1]