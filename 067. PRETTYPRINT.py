#PRETTYPRINT
"""
Print concentric rectangular pattern in a 2d matrix. 

Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.

Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
Example 2:

Input: A = 3.

Output:

3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3 
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        num = A
        arr = []
        er = A*2 -1
        ec = A*2 -1
        sr,sc = 0,0
        for i in range(er):
            arr.append([0]*ec)
        # print(arr)
        while sr <= er and sc<=ec:
            for col in range(sc,ec):
                arr[sr][col]=num
            for row in range(sr,er):
                arr[row][ec-1]=num
            for col in reversed(range(sc,ec)):
                if sr == er:
                    break
                arr[er-1][col]=num
            for row in reversed(range(sr,er)):
                if sc == ec:
                    break
                arr[row][sc]=num
            
            sr+=1
            sc+=1
            ec-=1
            er-=1
            num-=1
        return (arr)
