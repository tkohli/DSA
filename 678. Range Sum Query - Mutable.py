class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.total = sum(nums)  # 9

    def update(self, index: int, val: int) -> None:
        self.total += (val - self.nums[index])  # 8
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if right - left > len(self.nums) // 2:
            ans = sum(self.nums[:left]) + sum(self.nums[right + 1:])
            return self.total-ans
        else:
            return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
