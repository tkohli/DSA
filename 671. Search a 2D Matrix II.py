matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
    3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
"""
we can clearly see that if we do some clean implementation we can find ans
Naive - Binary search on each row O(n log m)
Failed approach reason We have values at mat[0][0],matrix[1][1]
But we given matrix with n,m len so we cannot use this logic
So now we start from first column last element the if val is greater than target 
r-=1 if val is less then target c+=1
https://assets.leetcode.com/users/brianchiang_tw/image_1583304443.png
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)-1
        c = 0

        while r >= 0 and c < len(matrix[0]):
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                r -= 1
            else:
                c += 1
        return False
