class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        curMax = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                curMax = 0
            totalTime += min(curMax, neededTime[i])
            curMax = max(curMax, neededTime[i])
        return totalTime

        # ans = 0
        # i, j = 0, 0
        # n = len(neededTime)
        # while i < n and j < n:
        #     curTotal = 0
        #     curMax = 0
        #     while j < n and colors[i] == colors[j]:
        #         curTotal += neededTime[j]
        #         curMax = max(curMax, neededTime[j])
        #         j += 1
        #     ans += curTotal-curMax
        #     i = j
        # return (ans)
