class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[-1]*(k+1) for _ in range(n)]

        def dfs(i,coins): #i = pile number
            # base case
            if i==n:
                return 0

            # if value in our dp then use it
            if dp[i][coins]!=-1:
                return dp[i][coins]
 

            dp[i][coins] = dfs(i+1,coins) # we went to go to next pile withoutt taking cur coin 
            # recursion

            curPile = 0
            for j in range(min(coins,len(piles[i]))):
                curPile += piles[i][j]
                dp[i][coins] = max(curPile + dfs(i+1, coins - j - 1), dp[i][coins])

            return dp[i][coins]

        return dfs(0, k)