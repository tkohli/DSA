# Remove Consecutive Characters
"""
Problem Description

Given a string A and integer B, remove all consecutive same characters that have length exactly B.



Problem Constraints
1 <= |A| <= 100000

1 <= B <= |A|



Input Format
First Argument is string A.

Second argument is integer B.



Output Format
Return a string after doing the removals.



Example Input
Input 1:

A = "aabcd"
B = 2
Input 2:

A = "aabbccd"
B = 2


Example Output
Output 1:

 "bcd"
Output 2:

 "d"


Example Explanation
Explanation 1:

 "aa" had length 2.
Explanation 2:

 "aa", "bb" and "cc" had length of 2.
"""
class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, a, b):
        s=''
        i=0
        while(i<len(a)):
            if(a[i:i+b]==a[i]*b):
                i+=b
                continue
            s+=a[i]
            i+=1
        return s

        # out = []
        # B = 2
        # A = list(A)
        # # print(A)
        # dct = {}
        # for a in A:
        #     if a in dct:
        #         dct[a]+=1
        #     else:
        #         dct[a] = 1
        # for element,value in dct.items():
        #     # print(element,value)
        #     if value>=B:
        #         continue
        #     else:
        #         out.append(element)
        # out.sort()
        # return "".join(map(str,out))