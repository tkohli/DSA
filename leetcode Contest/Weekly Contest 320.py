# Number of Unequal Triplets in Array
nums = [4, 4, 2, 4, 3]


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        cnt += 1
        return cnt
