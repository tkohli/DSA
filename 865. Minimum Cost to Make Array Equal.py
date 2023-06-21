class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        """
        Changing the elements into one of the numbers already existing in the 
        array nums is optimal.

        Try finding the cost of changing the array into each element,
        and return the minimum value

        similar to sliding window 
        nums = [1,3,5,2], cost = [2,3,1,14]

        numCost = [[1,2],
                   [2,14],
                   [3,3],
                   [5,1]]

        prefix = [2, 16, 19, 20]
        tmp = 24 -> 8 -> 20 ->56
        result=8
        
        """
        numCost = sorted([num,c] for num,c in zip(nums, cost))
        n = len(cost)
        prefix = [0]*n
        prefix[0] = numCost[0][1]

        for i in range(1,n):
            prefix[i] = numCost[i][1] + prefix[i-1]

        tmp = 0
        for i in range(1,n):
            tmp += numCost[i][1] * (numCost[i][0]- numCost[0][0])
        result = tmp
        print(tmp)

        for i in range(1,n):
            gap = numCost[i][0]- numCost[i-1][0]
            tmp += prefix[i-1]*gap
            tmp -= gap*(prefix[n-1]-prefix[i-1])
            result = min(tmp,result)
        
        return result

