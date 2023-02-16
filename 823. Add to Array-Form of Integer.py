class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        i = len(num)-1
        tmp = []
        while i >= 0 or k or carry :
            if i==-1:
                break
            t = k%10
            k//=10
            ans = (carry+num[i]+t)
            carry = ans//10
            num[i]=ans%10
            i-=1
        while carry or k:
            t = k%10
            k//=10
            ans = (carry+t)
            carry = ans//10
            tmp.append(ans%10)
        return tmp[::-1]+ num


        # ans = 0
        # for n in num:
        #     ans = (ans*10) + n
        # ans +=k
        # res = []
        # while ans:
        #     res.append(ans%10)
        #     ans //= 10
        # return res[::-1]

        