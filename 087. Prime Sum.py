# prime sum
"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s  conjecture

Example:


Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d] 

If a < c OR a==c AND b < d. 
"""
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        def prime(x):
            d = 2
            while(d*d<=x):
                if not x%d: return False
                d+=1
            return True
        for i in range(2,A//2+1):
            if prime(i) and prime(A-i): return [i,A-i]