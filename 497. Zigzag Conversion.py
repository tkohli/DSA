"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"

______________________
Solution we can think of this as some sort of mathematical logic but
there must be some smart/clever move around 1. We can use text{min}( text{numRows}, text{len}(s))min(numRows,len(s)) lists to represent the non-empty rows of the Zig-Zag Pattern.

Iterate through ss from left to right, appending each character to the appropriate row. The appropriate row can be tracked using two variables: the current row and the current direction.

The current direction changes only when we moved up to the topmost row or moved down to the bottommost row.
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lst = [""]*numRows
        curRow = 0
        goingDown = False
        for i, ch in enumerate(s):
            lst[curRow] += ch
            if curRow == 0 or curRow == numRows-1:
                goingDown = not goingDown
            if goingDown:
                curRow += 1
            else:
                curRow -= 1
        return "".join(lst)
