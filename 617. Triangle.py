"""
We start by end and then going up
Main idea is that from a ponit it can have 2 
possible ways but we keep the min val 
mat[i][j] += min(mat[i+1][j],mat[i+1][j+1])
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle)-1)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
                
        return triangle[0][0]