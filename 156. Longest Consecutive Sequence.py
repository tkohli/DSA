#Longest Consecutive Sequence
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        s = set(A)
        ans = 0
        for i in range(len(A)):
            if A[i]-1 not in s:
                j = A[i]
                while j in s:
                    j+=1
                ans = max(ans,j-A[i])
        return ans
                
