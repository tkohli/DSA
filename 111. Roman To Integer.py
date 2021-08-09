# Roman To Integer
"""
Given a string A representing a roman numeral.

Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.

NOTE: Read more 

details about roman numerals at Roman Numeric System




Input Format

The only argument given is string A.
Output Format

Return an integer which is the integer verison of roman numeral string.
For Example

Input 1:
    A = "XIV"
Output 1:
    14

Input 2:
    A = "XX"
Output 2:
    20
"""
class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        # x = "IVXLCDM"
        d = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        # print(d)
        ans = 0
        for i in range(len(A)-1):
            if d[A[i]] < d[A[i+1]]:
                ans -= d[A[i]]
            else:
                ans += d[A[i]]
        ans += d[A[len(A)-1]]
        return ans
            
# class Solution:
#     # @param A : string
#     # @return an integer
#     def romanToInt(self, A):
#         result=0
#         corr={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#         max=0
#         for c in reversed(A):
#             i = corr[c]
#             if(i>=max):
#                 result+=i
#             else:
#                 result-=i
#             if(i>max):
#                 max=i
#         return result
                