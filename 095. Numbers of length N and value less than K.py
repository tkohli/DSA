# Numbers of length N and value less than K
"""
Problem Description

Given a set of digits (A) in sorted order, find how many numbers of length B are possible whose value is less than number C.
NOTE: All numbers can only have digits from the given set.  

Examples:

Input:
  0 1 5

  1

  2

Output:

  2 (0 and 1 are possible)  


Input:
  0 1 2 5

  2

  21

Output:
  5 (10, 11, 12, 15, 20 are possible)

Constraints:

1 <= B <= 9, 0 <= C <= 1e9 & 0 <= A[i] <= 9

"""
import bisect
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    # def solve(self, A, B, C):
    def count(self, A, B, b, i):
        if i >= len(b) or B==0:
            return 1
        c_max = int(b[i])
        rt = 0
        for x in A:
            if i == 0 and x ==0 and B!=1:
                continue
            if x > c_max:
                continue
            if x == c_max:
                if i >= len(b) -1:
                    continue
                rt = rt + self.count(A, B-1, b, i+1)
            else:
                rt = rt + len(A)**(B-1)
        return rt
                
    
    def solve(self, A, B, C):
        c = str(C)
        if len(c) < B:
            return 0
        
        ind = 0
        if len(c) == B:
            return self.count(A, B, c, 0)
        rt = 0
        for x in A:
            if x == 0 and B!=1:
                continue
            if x==0 and x < C:
                rt +=1
            else:
                rt = rt + len(A)**(B-1)
        return rt
            