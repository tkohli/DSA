class Solution:
    def numberOfSteps(self, num: int) -> int:
        s = bin(num)[2:]
        return s.count('1') + len(s) - 1
        # count = 0
        # while num:
        #     if num%2==0:
        #         num//=2
        #         count+=1
        #     if num%2==1:
        #         num-=1
        #         count+=1
        # return count
