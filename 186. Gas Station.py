class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        if sum(A) < sum(B):
            return -1
        tank, start = 0, 0
        for i in range(len(A)):
            tank+= A[i] - B[i]

            if tank < 0:
                start = i+1
                tank = 0
        return start
