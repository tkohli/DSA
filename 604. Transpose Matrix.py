"""
It is easy to do this for n * n matrix but for m*n matrix 
we need to find out some better way of solving
"""


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        ans = [[0]*r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                ans[j][i] = matrix[i][j]
        return ans

        # return zip(*matrix)
