class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ord = list(nums)

    def reset(self) -> List[int]:
        self.nums[:] = (self.ord)
        print(self.ord)
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.nums)):
            swap_idx = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[swap_idx] = self.nums[swap_idx], self.nums[i]
        return self.nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
