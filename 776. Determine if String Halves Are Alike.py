class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)//2
        c=0
        for i in range(n):
            if s[i] in "aeiouAEIOU":
                c+=1
        for i in range(n,len(s)):
            if s[i] in "aeiouAEIOU":
                c-=1
        return c==0
        
