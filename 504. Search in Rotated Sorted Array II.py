from numpy import array


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
# since this is rotated that means we can use Binary search
# in order to do this we need to implement a binary search
# with more conditions


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return True

            if nums[l] == nums[m]:
                l += 1
                continue
            # now check if val is there in first
            pivotArray = nums[l] <= nums[m]
            targetArray = nums[l] <= target
            if pivotArray ^ targetArray:    # XOR Gate
                if pivotArray:
                    l = m+1
                else:
                    r = m-1
            else:
                if nums[m] < target:
                    l = m+1
                else:
                    r = m-1
        return False
