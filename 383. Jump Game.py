class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        jumps = 0
        steps = nums[0]
        maxReach = nums[0]
        for i, num in enumerate(nums):
            maxReach = max(maxReach, i+num)
            steps -= 1
            if steps < 0:
                return False
            if steps == 0:
                jumps += 1
                steps = maxReach-i
        return True


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 0
        steps = nums[0]
        maxReach = nums[0]
        for i in range(1, len(nums)-1):
            maxReach = max(maxReach, i+nums[i])
            steps -= 1
            if steps == 0:
                jumps += 1
                steps = maxReach-i
        return jumps+1
