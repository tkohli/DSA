class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for nm in nums:
            if nm <= first:
                first = nm
            elif nm <= second:
                second = nm
            else:
                return True
        return False
# for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] < nums[j] < nums[k]:
        #                 return True
        # return False

