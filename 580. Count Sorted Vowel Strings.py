"""
We will solve this question in 4 ways
The first one would be backtracking which was used in previous question
either recursion or looping 
"""


import math


class Solution:
    def countVowelStrings(self, n: int) -> int:
        def helper(n, comb):
            if n == 0:
                return 1
            cnt = 0
            for ch in ['a', 'e', 'i', 'o', 'u']:
                # check sorted
                if ch >= comb:
                    cnt += helper(n-1, ch)
            return cnt

        return helper(n, '')


"""
Now we will use memomization for DP based solution 
we start with 
[1,1,1,1,1]
a = 1 -> 5 -> 15 -> 35 ...
e = 1 -> 4 -> 10 -> 20 ...
i = 1 -> 3 -> 6 -> 10 ...
o = 1 -> 2 -> 3 -> 4 ...
u = 1 -> 1 -> 1 -> 1 ...
[0,0,0,0,0,0]
[0,1,2,3,4,5]
[0,1,0,0,0,0]
[0,1,0,0,0,0]
[0,1,0,0,0,0]
[0,1,0,0,0,0]

[0,0,0,0,0,0]
[0,1,2,3,4,5]
[0,1,3,6,10,15]
[0,1,0,0,0,0]
[0,1,0,0,0,0]
[0,1,0,0,0,0]


[0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 4, 5]
[0, 1, 3, 6, 10, 15]
[0, 1, 4, 10, 20, 35]
[0, 1, 5, 15, 35, 70]
[0, 1, 6, 21, 56, 126]
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 6 for _ in range(n+1)]
        for i in range(1, 6):
            dp[1][i] = i

        for i in range(2, n+1):
            dp[i][1] = 1
            for j in range(2, 6):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[n][5]

# same DP using constant space


class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1, 1, 1, 1, 1]
        for i in range(2, n+1):
            for j in range(5):
                arr[j] = sum(arr[j:])
        return sum(arr)


# mathematical solution
# https://assets.leetcode.com/users/images/e2537376-77ad-4a4d-be05-07c99acad58d_1620271631.6924222.png
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) // 24


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 4, 4)
