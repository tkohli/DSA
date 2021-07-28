# Count Negative Numbers in a Sorted Matrix
"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""

def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count= 0
        for arr in grid:
            for a in reversed(arr):
                if a < 0:
                    count+=1
                else:
                    break
            # for a in arr:
            #     if a < 0:
            #         count+=1
        return count