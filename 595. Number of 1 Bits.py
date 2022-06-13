class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count("1")
        # count = 0
        # while n:
        #     count+=1
        #     # n=n>>1
        #     n &= (n-1)
        # return count

# """
# 1011 & 1010 = 1010
# 1010 & 1001 = 1000
# 1000 & 0111 = 0000
# """
# while n:
#     n&=(n-1)
#     res += 1
# print(res)
