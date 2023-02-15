class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = 0
        for n in num:
            ans = (ans*10) + n
        ans +=k
        res = []
        while ans:
            res.append(ans%10)
            ans //= 10
        return res[::-1]