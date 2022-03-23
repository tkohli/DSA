class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minDiff = float("inf")
        nums.sort()
        for i in range(len(nums)-1):        # such that we have 3 elements always
            l = i+1
            r = len(nums)-1
            while l < r:
                curr = nums[i]+nums[l]+nums[r]
                if abs(curr-target) < minDiff:
                    minDiff = abs(curr-target)
                    ans = curr
                if curr > target:
                    r -= 1
                elif curr < target:
                    l += 1
                else:
                    return target
        return ans
