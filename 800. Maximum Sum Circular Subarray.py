class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # minSoFar = -3
        # maxSoFar = 7
        maxTotal, maxSoFar, minSoFar, minTotal, s = A[0], A[0], A[0], A[0], A[0]
        for i in range(1, len(A)):
            maxSoFar = max(A[i], maxSoFar + A[i])
            maxTotal = max(maxTotal, maxSoFar)

            minSoFar = min(A[i], minSoFar + A[i])
            minTotal = min(minTotal, minSoFar)
            s += A[i]
        if(s == minTotal):
            return maxTotal

        return max(s - minTotal, maxTotal)
        # return max(maxSofar, sum(nums)-minSoFar)

        # nums = nums + nums
        # ans = nums[0]
        # l = len(nums) // 2
        # for i in range(l ):
        #     tmp = 0
        #     for n in nums[i : i + l]:
        #         tmp = max(n, tmp + n)
        #         ans = max(ans, tmp)
        # # print(ans)
        # return ans
