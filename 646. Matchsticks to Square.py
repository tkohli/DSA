"""
Important points we have to use all matchsticks so 
total sum / 4 = side of square 
We do backtracking and in this we have 
"""
matchsticks = [1, 1, 2, 2, 2]


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks)//4
        sides = [0, 0, 0, 0]

        if sum(matchsticks)/4 != length:
            return False

        matchsticks.sort(reverse=True)

        def backTrack(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j]+matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backTrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False

        return backTrack(0)
