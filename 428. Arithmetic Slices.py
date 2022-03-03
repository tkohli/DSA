class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ap = [0 for _ in range(len(nums))]
        for idx in range(2,len(nums)):
            diff = nums[idx]-nums[idx-1]
            if nums[idx-1]-nums[idx-2] == diff:
                ap[idx] = ap[idx-1]+1
        return sum(ap)