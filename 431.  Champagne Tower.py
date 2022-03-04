"""
We are given tower of glasses in which we are poring 
Champagne and as it overflows it filles below glass
eg = 
                U           100%
            ---   ---
            |       |
          --U--   --U--     100%    100%
         |     | |     |
         U      U      U    25%     50%    25%
since 2nd glass gets 2 inputs hence it will get filled faster
Try to simulate the same in code


poured = 1, query_row = 1, query_glass = 1
o/p = 0 as only top glass is filled and no extra champagne is available

"""
poured = 1
query_row = 1
query_glass = 1
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        glass = [[0]*k for k in range(1,102)]
        glass[0][0] = poured
        for r in range(query_row):
            for c in range(r+1):
                temp = (glass[r][c]-1.0)/2.0   # Filling the prev 
                if temp>0:
                    glass[r+1][c] += temp
                    glass[r+1][c+1] += temp
        return min(1,glass[query_row][query_glass])