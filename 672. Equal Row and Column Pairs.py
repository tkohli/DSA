"""
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Main issue with this program is that we need to keep track of count
so lets do that with the help of counter
"""
from typing import Counter


grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
dct = Counter(tuple(row) for row in grid)  # also acts as default dct
ans = 0
for row in zip(*grid):
    ans += dct[tuple(row)]
print(ans)
