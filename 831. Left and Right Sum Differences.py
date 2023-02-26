# Left and Right Sum Differences
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ans = [nums[_] for _ in range(len(nums))]
        for i in range(1,len(nums)):
            ans[i]+=ans[i-1]
        print(ans)
        t = 0
        for i in range(len(nums)-1,-1,-1):
            t+=nums[i]
            ans[i] = abs(ans[i]-t)
        return ans