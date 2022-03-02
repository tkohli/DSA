class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums[1:])
        # starting by pivot  = 0
        temp = nums[0]
        idx = 0
        while idx < len(nums)-1:
            if leftSum == rightSum:
                return idx
            leftSum+=temp
            idx+=1
            temp = nums[idx]
            rightSum -= temp
        # edge case 
        leftSum = 0
        rightSum = sum(nums[:-1])
        if leftSum == rightSum:
            return len(nums)-1
        return -1