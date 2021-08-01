# Sorted Permutation Rank
"""
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 

Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003
"""
class Solution:
    # @param A : string
    # @return an integer
    def factorial(self,n):
        fact = 1
        if n == 1 or n==0:
            return fact
        for i in range(1,n+1):
            fact = fact*i
        return fact
        
    def findRank(self, A):
        M =1000003
        length = len(A)
        
        
        rank = 1
        f = self.factorial(len(A))
        l = len(A)
        #print arr
        for i in range(len(A)):
            count = 0
            for j in range(i+1,len(A)):
                if A[i] > A[j]:
                    count  = count + 1
                    
            rank = (rank + count* f/l)%M
            f = f/l
            l = l -1
            
        return rank
            