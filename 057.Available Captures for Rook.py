# Available Captures for Rook
"""
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.

 

Example 1:


Input: board = [[".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".","R",".",".",".","p"],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.
"""


def numRookCaptures(self, board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    cap = 0
    id = 0
    x = []
    y = []
    for line in board:
        if "R" in line:
            x = line
            id = (line.index("R"))
    for i in range(8):
        y.append(board[i][id])
    print(x, y)
    for i in range(id, 8):
        if x[i] == "B":
            break
        if x[i] == 'p':
            cap += 1
            break
    for i in range(id, -1, -1):
        if x[i] == "B":
            break
        if x[i] == 'p':
            cap += 1
            break
    for i in range(id, 8):
        if y[i] == "B":
            break
        if y[i] == 'p':
            cap += 1
            break
    for i in range(id, -1, -1):
        if y[i] == "B":
            break
        if y[i] == 'p':
            cap += 1
            break

    return (cap)
