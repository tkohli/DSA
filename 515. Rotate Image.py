from turtle import right


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
We are given a matrix and we have to change it's val such that it seems rotated 
this can bedone easily using 2nd matrix but question specifies that we must
do this in constant space
"""
l, r = 0, len(matrix) - 1
while l < r:
    top = l
    bottom = r
    for i in range(r-l):
        tmp = matrix[top][l+i]
        matrix[top][l+i] = matrix[bottom-i][l]
        matrix[bottom-i][l] = matrix[bottom][r-i]
        matrix[bottom][r-i] = matrix[top+i][r]
        matrix[top+i][r] = tmp
    l += 1
    r -= 1
