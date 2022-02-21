class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currentCount = 1
        currentMajority = nums[0]
        for num in nums[1:]:
            if num == currentMajority:
                currentCount += 1
            else:
                currentCount -= 1
                if currentCount == 0:
                    currentMajority = num
                    currentCount = 1
        return currentMajority
