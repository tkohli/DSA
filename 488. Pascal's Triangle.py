numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
start by making a triangle of 1's 
after row 2nd take prev row then add [0] to it's starting and ending
then add 2 number and update its val in ans array 
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1 for i in range(j)] for j in range(1, 1+numRows)]
        if numRows < 2:
            return ans
        for i in range(2, numRows):
            prev = [0]+ans[i-1]+[0]
            for j in range(len(ans[i])):
                ans[i][j] = prev[j]+prev[j+1]
        return ans
