class Solution:

    def longestPalindrome(self, s: str) -> str:

        def isPalin(s,i,j):

            while i>=0 and j<len(s) and  s[i]==s[j]:

                    i-=1

                    j+=1

            return j-i-1

        

        end= start = 0

        ans = ""

        for i in range(len(s)):

            odd = isPalin(s,i,i)

            even = isPalin(s,i,i+1)

            tmp = max(odd,even)

            if tmp > end-start:

                start = i-(tmp-1)//2

                end = i+ tmp//2

        return s[start:end+1]
