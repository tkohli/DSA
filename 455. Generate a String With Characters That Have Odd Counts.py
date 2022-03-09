class Solution:
    def generateTheString(self, n: int) -> str:
        ans = ""
        if n%2==1:
            for i in range(n):
                ans+='a'
        else:
            for i in range(n-1):
                ans+='a'
            ans+='b'
        return ans