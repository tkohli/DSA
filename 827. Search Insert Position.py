class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            else:
                right = mid-1
                
                
        if nums[mid]>target:   #6>7 False
            return mid
        else:
            return mid+1