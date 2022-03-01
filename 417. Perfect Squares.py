class Solution:
    def numSquares(self, n: int) -> int:
        nums = [float('inf') for i in range(n+1)]

        nums[0] = 0

        for num in range(1, n+1):
            for idx in range(1, num+1):
                if (idx*idx) > n:
                    break
                if 1 + nums[num-(idx*idx)] < nums[num]:
                    nums[num] = nums[num-(idx*idx)]+1
        return nums[-1]
