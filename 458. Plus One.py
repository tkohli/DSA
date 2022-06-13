class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for n in digits:
            num = num*10 + n
        num += 1
        return list(map(int, str(num)))

        # carry = 0
        # num = digits[-1] + 1
        # if num <= 9:
        #     digits[-1] = digits[-1]+1
        #     return digits
        # carry = 1
        # digits[-1] = 0
        # i = len(digits)-2
        # while i>=0:
        #     if digits[i] == 9 and carry == 1:
        #         digits[i] = 0
        #         carry = 1
        #     elif carry == 1:
        #         digits[i]+=1
        #         carry = 0
        #     i-=1
        # if carry == 1 and i == -1:
        #     digits.insert(0,1)
        # return digits
