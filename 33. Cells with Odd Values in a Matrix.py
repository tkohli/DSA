#Cells with Odd Values in a Matrix
 """
There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:

Increment all the cells on row ri.
Increment all the cells on column ci.
Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all locations in indices.

Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

"""

def oddCells(m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
#         rows = [0] * m
#         cols = [0] * n

#         for r,c in indices:
#             rows[r] += 1
#             cols[c] += 1

#         #iterate each cell, value = row value + col value, check odd or not
#         odd = 0
#         for ri in rows:
#             for ci in cols:
#                 if (ri+ci) % 2 == 1:
#                     odd += 1


#         return odd
        
        mat = np.zeros((m,n))
        for ind in indices:
            i,j = ind
            mat[i,:] = mat[i,:]+1
            mat[:,j] = mat[:,j]+1
            # mat[i,:] = mat[i][0]+1
            # mat[:][j] = mat[:][j]

        count = 0
        for ma in mat:
            for m in ma:
                if m%2==0:
                    pass
                else:
                    count+=1
        return (count)
        