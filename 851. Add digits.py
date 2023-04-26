class Solution:
    def addDigits(self, num: int) -> int:
        # 4th Formula
        # Time - O(1) || Space - O(1)

        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

        # 3rd int by DC and TK
        # Time - O(n) || Space - O(1)
        # while True:
        #     ans = 0
        #     while num:
        #         ans +=num%10
        #         num//=10
        #     if ans//10==0:
        #         return ans
        #     num=ans


        #2nd Loop by DC
        # Time - O(n) || Space - O(n)
        # while True:
        #     ans = 0
        #     for i in str(num):
        #         ans+=int(i)
        #     if ans in [0,1,2,3,4,5,6,7,8,9]: or ans//10==0
        #         return ans
        #     num=ans
        

        #1st Recursion by DC
        # Time - O(n) || Space - O(n)
        # def helper(num):
        #     ans = 0
        #     for i in str(num):
        #         ans+=int(i)
        #     if ans in [0,1,2,3,4,5,6,7,8,9]:
        #         return ans
        #     return helper(ans)
        
        # return helper(num)

        

