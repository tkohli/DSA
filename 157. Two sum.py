
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, k):
        diffs = {}
        for i, v in enumerate(A):
            if k - v in diffs:
                return diffs[k - v] + 1, i + 1
            elif v not in diffs:
                diffs[v] = i
        return []