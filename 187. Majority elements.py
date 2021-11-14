class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n = len(A)/2
        for a in A:
            if A.count(a) > n:
                return a
        # new = set(A)
        # for n in new:
        #     if A.count(n)>=len(A)//2:
        #         return n
