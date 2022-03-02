class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for char in s:
            if char.isalnum():
                n+=(char.lower())
        # if n==n[::-1]:
        #     print(True)
        i = 0
        j = len(n)-1
        print(n)
        while i<j:
            if n[i]!=n[j]:
                return False
            else:
                i+=1
                j-=1
        return True