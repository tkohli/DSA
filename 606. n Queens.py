"""
In the first solution we will follow the steps of solving 
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = [-1]*n
        """
        In this we will store  like [1, 3, 0, 2] means
        [.Q..]
        [...Q]
        [Q...]
        [..Q.]
        """

        def backTrack(index):
            if index == len(queens):
                res.append(queens[:])
                return
            for i in range(len(queens)):
                queens[index] = i
                if valid(index):
                    backTrack(index+1)

        def valid(n):
            for i in range(n):
                if abs(queens[i]-queens[n]) == abs(n-i):  # same Diagonal
                    return False
                if queens[i] == queens[n]:  # same col
                    return False
            return True

        # now we have queens = [1,3,0,2] this function returns
        def makeBoard(queens):
            n = len(queens)
            board = []
            boardTmp = [['.']*n for _ in range(n)]
            for r, c in enumerate(queens):
                boardTmp[r][c] = 'Q'
            for row in boardTmp:
                board.append("".join(row))
            return board

        def make_all_boards(res):
            actual_boards = []
            for queens in res:
                actual_boards.append(makeBoard(queens))
            return actual_boards

        backTrack(0)
        return make_all_boards(res)


"""
In this second solution we will use set and keep this simple 
Goal: Place a queen somewhere such that no queen are attacking each other
Approach: backtracking
- each recursive layer will decide on a row and also the placement of the queen
- the constraint is making sure we do not place a queen where its in sight of another queen. How?
    1) make sure it is not on the same column --> create a column set
    2) make sure it is not in same diagonal path --> create a diagonal set (calculated via r+c)
    3) make sure it is not in a antidiagonal path --> create a antidiagonal set (calculated via r-c)
    
    We dont need to worry about rows because it is handled by the backtracking parameter that always recurse
    to next level of the row
    
    ** note: if you dont know why r+c and r-c are diagonal paths --> Draw it out and check why it does!! 
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        if n == 0:
            return []

        col = set()
        diagonal = set()    # determined by r+c
        antidiagonal = set()
        output = []
        result = []

        def backtrack(r):
            nonlocal n, col, diagonal, antidiagonal, output, result
            if r == n:
                result.append(output[:])
                return

            for c in range(n):
                if c in col or (r+c) in diagonal or (r-c) in antidiagonal:
                    continue

                col.add(c)
                diagonal.add(r+c)
                antidiagonal.add(r-c)
                output.append('.'*c + 'Q' + '.'*(n-c-1))
                backtrack(r+1)

                col.remove(c)
                diagonal.remove(r+c)
                antidiagonal.remove(r-c)
                output.pop()

        backtrack(0)
        return result

        dic = {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 9: 352}
        return dic[n]
